# Iteration Helpers

## Definition
Built-in and `itertools` helpers that produce or transform iterables lazily. All Python 3 sequence-like helpers (`range`, `map`, `filter`, `zip`, `enumerate`, `reversed`) return iterators / lightweight views — no intermediate list is built.

## `range(stop)` / `range(start, stop)` / `range(start, stop, step)`
Lazy arithmetic sequence of ints; `stop` is exclusive; `step` may be negative.
```python
list(range(5))              # [0, 1, 2, 3, 4]
list(range(2, 7))           # [2, 3, 4, 5, 6]
list(range(0, 10, 2))       # [0, 2, 4, 6, 8]
list(range(5, 0, -1))       # [5, 4, 3, 2, 1]
```
Supports `len`, indexing, slicing, and `x in r` in **O(1)** (arithmetic check, not linear scan). `range(10**18)` is fine — no memory cost.

## `enumerate(iterable, start=0)`
Yields `(index, value)`. Use instead of `range(len(x))` whenever you need the value too.
```python
for i, fruit in enumerate(["a", "b", "c"], start=1):
    print(i, fruit)
```

## `zip(*iterables, strict=False)`
Parallel iteration; yields tuples. Stops at the **shortest** input by default — silently drops leftovers from longer inputs.
```python
list(zip([1, 2, 3], ["a", "b"]))       # [(1, 'a'), (2, 'b')]  — 3 dropped
```
`strict=True` (3.10+) raises `ValueError` on length mismatch. Use it when unequal lengths would be a bug.
```python
list(zip(a, b, strict=True))
```

Unzipping via `*`:
```python
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)         # ('a','b','c'), (1,2,3)
```
Building a dict:
```python
dict(zip(names, ages))                 # {'Alice': 30, ...}
```

## `reversed(seq)`
Iterator over `seq` in reverse. Works on sequences with `__reversed__` or `__len__` + `__getitem__` — **not** on arbitrary iterators. `dict` gained `__reversed__` in 3.8; before that, `reversed(some_dict)` raised `TypeError`.
```python
list(reversed([1, 2, 3]))              # [3, 2, 1]
```

## `sorted(iterable, key=..., reverse=...)`
Returns a **new list**, sorted. Stable. `key=fn` computes a sort key per element (called once per element — cache-friendly). `reverse=True` for descending.
```python
sorted(words, key=str.lower)
sorted(items, key=lambda x: (x.priority, x.name))
```

## `map` / `filter`
Lazy iterators (Python 3). `map(fn, iter)` applies `fn`; `filter(fn, iter)` keeps truthy elements; `filter(None, iter)` drops falsy.
```python
list(map(str.upper, ["a", "b"]))       # ['A', 'B']
list(filter(None, [0, 1, "", "x"]))    # [1, 'x']
```
Comprehensions are usually clearer than `map`/`filter` with a `lambda`.

## `itertools` — power tools
All lazy; combine into pipelines.

**Chaining / slicing:**
```python
from itertools import chain, islice
list(chain([1, 2], [3, 4]))            # [1, 2, 3, 4]
list(chain.from_iterable([[1, 2], [3]]))   # flatten one level
list(islice(iter, 2, 10, 2))           # slice any iterable — no __getitem__ needed
```

**Grouping — consecutive keys only:**
```python
from itertools import groupby
data = sorted(rows, key=lambda r: r.dept)      # sort first!
for dept, group in groupby(data, key=lambda r: r.dept):
    print(dept, list(group))
```

**Combinatorics:**
```python
from itertools import product, permutations, combinations, combinations_with_replacement
list(product([0, 1], repeat=3))         # cartesian product
list(permutations("abc", 2))            # ordered, no repeats
list(combinations("abc", 2))            # unordered, no repeats
list(combinations_with_replacement("abc", 2))
```

**Accumulation / infinite:**
```python
from itertools import accumulate, count, cycle, repeat
list(accumulate([1, 2, 3, 4]))          # running sum: [1, 3, 6, 10]
list(accumulate([1, 2, 3], max))        # running max
# count(10), cycle("ab"), repeat(0, 5)  — infinite / bounded generators
```

**Zip variants and pairs:**
```python
from itertools import zip_longest, pairwise, tee
list(zip_longest("abc", [1, 2], fillvalue=0))   # [('a',1),('b',2),('c',0)]
list(pairwise("abcd"))                          # [('a','b'),('b','c'),('c','d')]  (3.10+)
a, b = tee(iter, 2)                             # split one iterator in two (buffers)
```

## Semantics
- Iterators are **one-shot** — exhaust once, then further `next()` raises `StopIteration`.
- `for` calls `iter()` once, then `next()` until `StopIteration`.
- `zip`, `map`, `filter`, `enumerate` in Python 3 are iterators; wrap in `list()` to materialize.
- `tee` buffers elements — costly if consumers diverge widely.

## Gotchas
- **`range` is not a list** — `range(3) + range(3)` fails; wrap in `list(...)` if you need concatenation.
- **`zip` truncates silently** — use `strict=True` when lengths must match.
- **`range(len(x))`** is a smell — use `enumerate(x)` when you also need the value.
- **Iterators exhaust** — once drained, a second pass yields nothing. Rebuild or store as a list if you need to reiterate.
- **`groupby` groups only consecutive keys** — sort by the same key first, otherwise groups fragment.
- **`enumerate(x, 1)`** — the second arg is `start`; prefer `start=1` for clarity.
- **`zip(*[])`** — unpacking an empty list yields no arguments and an empty iterator.
- **`tee` on a large iterator with slow consumers** buffers everything between them — memory blow-up.
