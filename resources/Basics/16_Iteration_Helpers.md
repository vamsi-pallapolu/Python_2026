# Iteration Helpers — `range`, `enumerate`, `zip`

## Why these three?
`range`, `enumerate`, and `zip` are three helpers you'll use in almost every `for` loop:
- **`range`** — generate a sequence of numbers (`0, 1, 2, ...`).
- **`enumerate`** — get the **index and value** while looping over a list.
- **`zip`** — loop over **two lists side by side**.

## `range(stop)` / `range(start, stop)` / `range(start, stop, step)`
Generates an arithmetic sequence of integers. `stop` is exclusive.
```python
list(range(5))              # [0, 1, 2, 3, 4]
list(range(2, 7))           # [2, 3, 4, 5, 6]
list(range(0, 10, 2))       # [0, 2, 4, 6, 8]
list(range(5, 0, -1))       # [5, 4, 3, 2, 1]
```

Typical use in a loop:
```python
for i in range(3):
    print(i)                # 0, 1, 2
```

Notes:
- `range` returns a `range` object, **not a list** — memory-efficient regardless of size (`range(10**9)` is fine).
- It supports `len()`, `in`, indexing, and slicing.

## `enumerate(iterable, start=0)`
Pair each element with its index. Cleaner than manually tracking a counter.
```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

Custom start:
```python
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
# 1 apple
# 2 banana
# 3 cherry
```

Anti-pattern to avoid:
```python
# Don't:
for i in range(len(fruits)):
    print(i, fruits[i])
# Do:
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

## `zip(*iterables)`
Iterate over multiple iterables **in parallel**, yielding tuples.
```python
names = ["Alice", "Bob", "Carol"]
ages  = [30, 25, 40]

for name, age in zip(names, ages):
    print(name, age)
# Alice 30
# Bob 25
# Carol 40
```

Stops at the **shortest** input by default:
```python
list(zip([1, 2, 3], ["a", "b"]))
# [(1, 'a'), (2, 'b')]        ← the 3 is dropped
```

`zip(..., strict=True)` (Python 3.10+) raises `ValueError` if lengths differ — use it when unequal lengths would be a bug.

## Building a dict from parallel lists
```python
dict(zip(names, ages))
# {'Alice': 30, 'Bob': 25, 'Carol': 40}
```

## Unzipping — the transpose trick
```python
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
# letters == ('a', 'b', 'c')
# numbers == (1, 2, 3)
```

## Combining all three
```python
names = ["Alice", "Bob", "Carol"]
scores = [90, 75, 85]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name}: {score}")
# 1. Alice: 90
# 2. Bob: 75
# 3. Carol: 85
```

## Related helpers to keep in mind
| Helper | What it does |
|--------|-------------|
| `reversed(seq)` | iterate in reverse; returns an iterator |
| `sorted(iter, key=..., reverse=...)` | sort into a new list |
| `map(fn, iter)` | apply `fn` to each element, lazily |
| `filter(fn, iter)` | keep elements where `fn(x)` is truthy, lazily |
| `itertools.chain(a, b)` | iterate over `a` then `b` |
| `itertools.zip_longest(a, b, fillvalue=None)` | zip that pads the shorter with `fillvalue` |

## Gotchas
- **`range` is not a list** — `range(3) + range(3)` fails. Convert with `list(range(...))` if you truly need a list.
- **`zip` silently truncates** — mismatched lengths are lost data. Use `strict=True` (3.10+) or `itertools.zip_longest` if that matters.
- **`enumerate(x, 1)` is positional** — the second arg is `start`, not "count". Prefer `start=1` for clarity.
- **`zip(*pairs)` needs at least one pair** — unpacking an empty list yields no arguments and returns an empty iterator.
- **All three return iterators (or iterator-like objects) in Python 3.** Wrapping in `list(...)` is fine for small data; don't do it for huge sequences.
