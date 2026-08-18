# Generators & the Iterator Protocol

## What is a generator?
A **generator** is a function that produces values **one at a time** instead of all at once. You write it like a normal function, but use `yield` instead of `return`. Great for looping over huge or endless sequences without loading everything into memory.

## The iterator protocol
Any object is an **iterator** if it implements:
- `__iter__(self)` — returns the iterator itself.
- `__next__(self)` — returns the next value, or raises `StopIteration`.

An **iterable** is anything you can call `iter()` on (lists, dicts, files, generators, ...). `for` loops call `iter()` and then `next()` under the hood.

```python
xs = [10, 20, 30]
it = iter(xs)               # get an iterator
next(it)                    # 10
next(it)                    # 20
next(it)                    # 30
next(it)                    # StopIteration
```

## Generator functions — `yield`
Any function containing `yield` becomes a **generator function**. Calling it returns a generator object; the body doesn't run until you iterate.
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i             # produce i, pause here until next(...)
        i += 1

g = count_up_to(3)
next(g)                     # 1
next(g)                     # 2
next(g)                     # 3
next(g)                     # StopIteration
```

Idiomatic use — iterate with `for`:
```python
for x in count_up_to(3):
    print(x)                # 1, 2, 3
```

## Generator expressions
Same syntax as a list comprehension, but with **parentheses** instead of brackets. Produces a generator object rather than materializing a list.
```python
squares = (x * x for x in range(1_000_000))    # cheap — no list built
sum(squares)                                    # iterates, doesn't allocate a list

# Compare with the list comprehension:
squares = [x * x for x in range(1_000_000)]    # builds the whole list first
```

Passing a generator expression as a **sole argument** lets you drop the extra parens:
```python
sum(x * x for x in range(10))       # OK
sum((x * x for x in range(10)))     # also OK
```

## Why generators?
- **Memory** — process an infinite or huge sequence without holding it all at once.
- **Composition** — chain generators end-to-end; data flows through pipeline-style.
- **Early exit** — consumers can stop after N items without work being done for the rest.

Example — reading a huge log file lazily:
```python
def parse_errors(path):
    with open(path, encoding="utf-8") as f:
        for line in f:                          # lines yielded lazily
            if "ERROR" in line:
                yield line.rstrip()

for err in parse_errors("big.log"):             # constant memory
    print(err)
```

## Multiple `yield`s
A generator can `yield` from many places; each `yield` pauses and resumes on the next `next()`.
```python
def sequence():
    yield "start"
    for i in range(3):
        yield i
    yield "end"

list(sequence())                # ['start', 0, 1, 2, 'end']
```

## `yield from` — delegate to another iterable
Flattens generator chains — everything yielded by the inner iterable is yielded by the outer.
```python
def sub():
    yield 1
    yield 2

def top():
    yield 0
    yield from sub()            # equivalent to: for x in sub(): yield x
    yield 3

list(top())                     # [0, 1, 2, 3]
```

## Generator vs list comprehension
| | Generator expression | List comprehension |
|---|---|---|
| Syntax | `(x*2 for x in xs)` | `[x*2 for x in xs]` |
| Result | iterator | list |
| Memory | O(1) at a time | O(n) — all at once |
| Reusable? | one-shot — exhausts after iteration | reusable — it's a real list |
| Indexable? | no | yes (`result[0]`) |

Use a **generator** when you only iterate once, care about memory, or work with unbounded streams. Use a **list** when you'll iterate multiple times, index into it, or need `len()`.

## Generators are one-shot
Once exhausted, they're done. To iterate again, create a new generator.
```python
g = (x for x in range(3))
list(g)         # [0, 1, 2]
list(g)         # []      ← already exhausted
```

## Gotchas
- **Calling a generator function doesn't run its body.** It returns a generator object; the body runs only when you iterate.
- **Generators are one-shot.** Loop over the same generator twice → the second loop sees nothing.
- **`yield` inside a `try/finally`** — the `finally` runs when the generator is closed (either exhausted or garbage-collected). Useful for cleanup, but subtle.
- **`return` inside a generator** — ends iteration; if you `return value`, that value becomes the `.value` on the `StopIteration` (rare — mostly used with `yield from`).
- **You can't index a generator.** `g[0]` fails; convert with `list(g)` first (defeating the purpose) or use `next(g)`.
- **Don't confuse `(x for x in ...)` with `(x,)`** — the first is a generator expression, the second is a one-element tuple.
