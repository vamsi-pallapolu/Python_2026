# Iteration

Source: `DataStructures/2_1_iteration.py`

## Definition
Iteration is **traversing an iterable one element at a time**. Python's primary construct is `for`; `while` handles condition-driven loops.

## Iterator protocol
- An **iterable** implements `__iter__()`, which returns an **iterator**.
- An **iterator** implements `__next__()`, which returns the next value or raises `StopIteration`.
- Sequence-protocol fallback: an object with `__getitem__` starting from index 0 is also iterable (legacy path).

## How `for` works
`for x in iterable:` desugars to:
```python
it = iter(iterable)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # loop body
```
So `for` handles both true iterators and legacy sequence types transparently.

## `for x in iterable` — direct
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

## `enumerate` — index + value
```python
for i, x in enumerate(['a', 'b', 'c'], start=0):
    print(i, x)
```
Preferred over `range(len(x))` when you need both — one lookup instead of two.

## `while` — condition-driven
Use when termination depends on runtime state, not a sequence.
```python
n = 0
while n < 3:
    print(n)
    n += 1
```
No `++` / `--` in Python. `++n` parses as unary-plus twice — a no-op.

## `range(len(x))` — anti-pattern for value+index
```python
for i in range(len(elements)):     # two lookups: elements[i]
    print(elements[i])
```
Prefer `enumerate`. Reach for `range(len(...))` only when you truly need just the indices (parallel structures, in-place index-based updates).

## Loop control
| Keyword | Effect |
|---------|--------|
| `break` | exit the innermost loop immediately |
| `continue` | skip to the next iteration |
| `pass` | no-op placeholder |
| `else` on a loop | runs iff the loop finished **without** `break` |

```python
for n in nums:
    if n == target:
        break
else:
    raise ValueError("not found")
```

## Iterating other types
```python
for ch in "abc":              # string -> characters
    ...

d = {"a": 1, "b": 2}
for k in d:                   # keys (default)
    ...
for v in d.values():
    ...
for k, v in d.items():
    ...

for x in {1, 2, 3}:           # set (arbitrary order)
    ...
for i in range(3):            # lazy integer sequence
    ...
for x in (i * i for i in range(5)):    # generator expression
    ...
for line in open("f.txt"):    # file object -> lines
    ...
```

## Iterables vs iterators
- **Iterables** can be re-iterated — each `iter(iterable)` call returns a fresh iterator (`list`, `str`, `dict`, `range`, ...).
- **Iterators** are single-shot — once exhausted, further `next` calls raise `StopIteration`. Generators and `zip`, `map`, `filter` return iterators.

```python
it = iter([1, 2, 3])
list(it)     # [1, 2, 3]
list(it)     # []   -- exhausted
```

## Two-argument forms
```python
next(it, default)           # returns default instead of StopIteration
iter(callable, sentinel)    # calls callable() until it returns sentinel
```
`iter(callable, sentinel)` is useful for polling loops:
```python
for line in iter(input, "quit"):
    print(line)
```

## Comprehension scope
Comprehension loop variables are **scoped to the comprehension** — they do not leak.
```python
[x for x in range(3)]
print(x)         # NameError
```
Plain `for` variables **do** leak into the enclosing scope:
```python
for i in range(3): pass
print(i)         # 2
```

## Gotchas
- **Mutating while iterating** — insertions/deletions skip or repeat elements. Iterate a copy (`a[:]`) or accumulate and reassign.
- **One-shot iterators** — you can't reuse an exhausted iterator; rebuild it.
- **Loop variable leaks** in plain `for` loops; comprehensions don't leak.
- **No `++` / `--`** — use `x += 1`.
- **Infinite `while`** — missing state change (`while i < n:` with no `i += 1`).
