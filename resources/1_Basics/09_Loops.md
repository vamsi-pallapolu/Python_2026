# Loops

Source: `Basics/7_loops.py`

## Definition
A loop repeatedly executes a block of statements. Python has two constructs:
- `for` — iterates over an iterable (list, tuple, string, range, dict, generator).
- `while` — executes while a boolean condition is `True`.

Use `for` when the iterable is known; use `while` when termination depends on runtime state.

## `for` loop
Iterates element-by-element; no manual index management.
```python
for x in [10, 20, 30]:
    print(x)

for i in range(3):        # 0, 1, 2
    print(i)

for ch in "abc":          # iterates characters
    print(ch)
```

Index + value with `enumerate`:
```python
for i, x in enumerate(["a", "b", "c"], start=0):
    print(i, x)
```

Parallel iteration with `zip` (stops at shortest input; `strict=True` in 3.10+ raises on length mismatch):
```python
for name, age in zip(["Ann", "Bob"], [30, 25]):
    print(name, age)
```

## `while` loop
```python
n = 0
while n < 3:
    print(n)
    n += 1
```

`while True` with an internal `break` — used when the exit condition is discovered inside the block:
```python
while True:
    line = input()
    if line == "quit":
        break
```

## `break` and `continue`
- `break` — terminates the innermost enclosing loop.
- `continue` — skips to the next iteration of the innermost enclosing loop.

```python
for x in [1, 2, 3, 4, 5]:
    if x == 3:
        continue
    if x == 5:
        break
    print(x)              # 1, 2, 4
```

Python has no labelled `break`. To exit multiple nested loops, encapsulate them in a function and `return`.

## `for ... else` and `while ... else`
The `else` clause executes only when the loop terminates without `break`. Typical use: search loops.
```python
for x in nums:
    if x == target:
        break
else:
    raise ValueError("target not found")
```

## Nested loops
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

## `range()`
Lazy integer sequence; `stop` is exclusive.
```python
range(stop)
range(start, stop)
range(start, stop, step)      # step may be negative
```
`range` supports `len()`, indexing, slicing, and `in` — the last runs in O(1) (arithmetic check), not O(n).

## Comprehensions
Expression form of a `for` loop that constructs a container. Supports optional filter and nested clauses.

```python
squares = [x*x for x in range(5)]                    # list
evens   = [x for x in nums if x % 2 == 0]            # filter
labels  = ["even" if x % 2 == 0 else "odd" for x in nums]  # ternary in expression
pairs   = [(i, j) for i in range(3) for j in range(3)]     # nested loop
flat    = [x for row in matrix for x in row]         # flatten

by_len  = {name: len(name) for name in names}        # dict comprehension
uniq    = {c for c in text}                          # set comprehension
gen     = (x*x for x in range(5))                    # generator expression
```
Comprehensions introduce their own scope — the loop variable does not leak.

## Semantics of `for`
A `for` loop is equivalent to:
```python
it = iter(iterable)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # loop body
```
Any object implementing `__iter__` (or the legacy `__getitem__` sequence protocol) is iterable.

## Gotchas
- **Mutating a sequence while iterating** — insertions/deletions cause skipped or repeated elements. Iterate a copy (`items[:]`) or accumulate results and reassign.
- **`range(len(x))` when the value is also needed** — use `enumerate(x)`.
- **Loop variable leaks** — after a plain `for i in ...`, `i` remains bound in the enclosing scope. Comprehensions do not leak.
- **No `++` / `--` operators** — use `i += 1`. `++i` parses as unary-plus twice; it's a no-op.
- **`while` without a state change** — the classic infinite loop.
