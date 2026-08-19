# Generators & the Iterator Protocol

## Definition
A **generator** is a function containing `yield`; calling it returns a **generator object** without running the body. The body advances on each `next()` and pauses at each `yield`, preserving local state. When the body returns, `next()` raises `StopIteration`.

## The iterator protocol
- `__iter__(self)` — returns an iterator (often `self`).
- `__next__(self)` — returns the next value or raises `StopIteration`.

An **iterable** is anything `iter()` accepts (has `__iter__`, or the legacy `__getitem__` sequence protocol). A `for` loop is:
```python
it = iter(iterable)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # body
```

Manual driving:
```python
it = iter([10, 20, 30])
next(it)    # 10
next(it)    # 20
next(it)    # 30
next(it)    # StopIteration
```

## Generator functions — `yield`
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i             # pause here; resume on next()
        i += 1

g = count_up_to(3)
next(g)                     # 1
list(g)                     # [2, 3]
```
Idiomatic — drive with `for`:
```python
for x in count_up_to(3):
    print(x)
```

Multiple `yield`s in one function are allowed; each pauses independently.
```python
def sequence():
    yield "start"
    for i in range(3):
        yield i
    yield "end"
list(sequence())            # ['start', 0, 1, 2, 'end']
```

## Generator expressions
Same syntax as a list comprehension, but with **parentheses**. Produces a generator, not a list — O(1) memory.
```python
squares = (x * x for x in range(1_000_000))
sum(squares)                # streams; no list built
```
When the generator expression is the **sole argument** to a call, the outer parens can be dropped:
```python
sum(x * x for x in range(10))
```

## `yield from`
Delegates iteration to another iterable — yields everything the sub-iterable yields, forwards `.send`, `.throw`, `.close` calls to the sub-generator, and propagates the sub-generator's return value.
```python
def sub():
    yield 1
    yield 2
    return "done"

def top():
    yield 0
    result = yield from sub()   # receives sub()'s return value
    yield 3
    yield result

list(top())                     # [0, 1, 2, 3, 'done']
```

## Memory vs list comprehension
| | Generator | List comp |
|---|---|---|
| Syntax | `(x*2 for x in xs)` | `[x*2 for x in xs]` |
| Result | iterator | list |
| Memory | one item at a time | all at once |
| Reusable | no — one-shot | yes |
| Indexable | no | yes |

Use a generator for large or unbounded streams and single-pass consumption. Use a list when you need `len`, indexing, or multiple iterations.

## `.send(value)` — two-way communication
Inside the generator, `yield` can be an **expression** whose value is what the caller passes to `.send()`. Advances one step, like `next()`, but injects a value.
```python
def echo():
    while True:
        received = yield        # yields None; receives caller's value
        print("got:", received)

g = echo()
next(g)                         # prime — advance to the first yield
g.send("hi")                    # prints "got: hi"
```
The first `.send(x)` must be `.send(None)` (or `next(g)`) because there's no `yield` waiting yet.

## `.throw(ExcType, ...)`
Raises the exception **at the current `yield`** inside the generator. If the generator catches it, execution continues; if not, the exception propagates back to the caller.

## `.close()`
Raises `GeneratorExit` at the current `yield`. The generator should let it propagate (typical `try/finally` cleanup path); catching and yielding again raises `RuntimeError`.
```python
def resource():
    try:
        yield open_thing()
    finally:
        close_thing()           # runs on .close() or GC
```

## `return` inside a generator
Ends iteration and sets `StopIteration.value` to the returned value. Not a plain return — the caller sees `StopIteration`, not the value, unless they use `yield from` (which extracts it) or catch `StopIteration` manually.
```python
def gen():
    yield 1
    return "done"

g = gen()
next(g)                         # 1
try:
    next(g)
except StopIteration as e:
    print(e.value)              # 'done'
```

## Debugging state
```python
import inspect
inspect.getgeneratorstate(g)
# 'GEN_CREATED' | 'GEN_RUNNING' | 'GEN_SUSPENDED' | 'GEN_CLOSED'
```

## Async generators (3.6+)
`async def` + `yield`; iterated with `async for`. Cannot use `yield from`; use `async for` inside instead.
```python
async def stream(urls):
    for u in urls:
        yield await fetch(u)

async for page in stream(urls):
    ...
```

## Semantics
- Calling a generator function **does not run the body** — it returns a generator object.
- Body runs on `next()` / `.send()` up to the next `yield`, which suspends the frame with locals intact.
- Exhausted generators raise `StopIteration` on every subsequent `next()`.
- `for x in gen:` consumes the generator; a second `for` sees nothing.

## Gotchas
- **Calling the function doesn't execute it** — you must iterate.
- **One-shot** — iterate twice and the second pass is empty.
- **No indexing** — `g[0]` fails; use `next(g)` or `list(g)` (defeats laziness).
- **`return value` in a generator** — ends iteration, sets `StopIteration.value`; the value is not returned to the immediate caller of `next()`.
- **`yield` inside `try/finally`** — `finally` runs on `.close()` or on garbage collection, not immediately after the last `yield`.
- **`(x for x in xs)` vs `(x,)`** — first is a generator, second is a one-element tuple.
- **First `.send` must be `None`** — otherwise `TypeError`; prime with `next(g)`.
- **`await` in a generator (non-async)** — not allowed; use `async def`.
