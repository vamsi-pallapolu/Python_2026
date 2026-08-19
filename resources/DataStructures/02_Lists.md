# Lists

Source: `DataStructures/2_0_list.py`

## Definition
A `list` is a **mutable, ordered sequence of arbitrary objects**. Elements are references — any type is allowed, and duplicates are fine.

## Creation
```python
a = [1, 2, 3]              # literal
b = list((4, 5, 6))        # from any iterable
c = [0] * 3                # [0, 0, 0]
d = []                     # empty
```
`[obj] * n` repeats the same **reference** `n` times — safe for immutables (`[0]*n`), dangerous for mutables (`[[]]*n` shares one inner list).

## Indexing and slicing
Zero-based; negative indices count from the end. Out-of-range indexing raises `IndexError`; slicing clamps.
```python
a = [0, 1, 2, 3, 4, 5]
a[0]        # 0
a[-1]       # 5
a[1:4]      # [1, 2, 3]   -- new list
a[::-1]     # [5, 4, 3, 2, 1, 0]
```
Slice assignment inserts, replaces, or deletes ranges:
```python
a[1:3] = [99]        # replace two items with one
a[1:1] = [8, 9]      # insert
del a[1:3]           # delete
```

## Adding elements
| Method | Effect | Cost |
|--------|--------|------|
| `a.append(x)` | append `x` to the end | O(1) amortized |
| `a.insert(i, x)` | insert before index `i` | O(n) |
| `a.extend(iter)` | append each item of `iter` | O(k) |
| `a += iter` | equivalent to `extend` (in-place) | O(k) |

```python
a = [1, 2, 3]
a.append(4)             # [1, 2, 3, 4]
a.insert(1, 9)          # [1, 9, 2, 3, 4]
a.extend([10, 20])      # [1, 9, 2, 3, 4, 10, 20]
```

## Removing elements
| Operation | Effect |
|-----------|--------|
| `a.remove(x)` | remove **first** occurrence of value `x`; raises `ValueError` if missing |
| `a.pop(i=-1)` | remove and **return** item at index `i` (default last) |
| `del a[i]` / `del a[i:j]` | remove by index or slice |
| `a.clear()` | remove all |

`remove` takes a **value**; `pop` and `del` take an **index**.

## Updating and membership
```python
a[1] = 10                # assign by index
x in a                   # O(n) linear scan
```
Use a `set` if you scan for membership repeatedly.

## Copying
Slicing and the copy methods produce a **shallow** copy — outer list is new, inner references are shared.
```python
b = a.copy()
b = list(a)
b = a[:]
import copy
b = copy.deepcopy(a)     # independent nested structures
```

## Sorting and reversing
```python
a.sort()                 # in-place; returns None
sorted(a)                # new list; original unchanged
a.sort(key=len, reverse=True)
a.reverse()              # in-place
a[::-1]                  # reversed copy
```
Timsort is stable — equal keys keep original order.

## Iteration
```python
for x in a:              # values
    ...
for i, x in enumerate(a):
    ...
```

## Comprehensions
Expression form of a `for` loop that builds a new list. Optional filter, ternary transform, nested clauses.
```python
[x * 2 for x in a]                        # transform
[x for x in a if x % 2 == 0]              # filter
["even" if x % 2 == 0 else "odd" for x in a]   # ternary transform
[(i, j) for i in range(3) for j in range(3)]   # nested loops
[x for row in mat for x in row]           # flatten
```
Trailing `if` filters; `if/else` in the expression transforms. Nested `for` clauses read left-to-right.

## Complexity
| Op | Cost |
|----|------|
| `a[i]`, `a[i] = x`, `len(a)` | O(1) |
| `a.append(x)` | O(1) amortized |
| `a.pop()` | O(1) |
| `a.pop(0)`, `a.insert(0, x)`, `a.remove(x)` | O(n) |
| `x in a` | O(n) |
| `a.sort()` / `sorted(a)` | O(n log n) |

For O(1) both-end operations use `collections.deque`. For repeated ordered-lookup use `bisect`.

## Gotchas
- **Mutating methods return `None`** — `a = a.append(4)` sets `a` to `None`.
- **`[[]] * n` aliases the inner list** — mutating one row mutates all. Use `[[] for _ in range(n)]`.
- **`remove` vs `del` vs `pop`** — value vs index; only `pop` returns the removed item.
- **Assignment is not a copy** — `b = a` shares the list. `a.copy()` / `list(a)` / `a[:]` are shallow; `copy.deepcopy` for nested.
- **Comprehensions are not always faster** — for side-effect-only loops (writing to a file, mutating state) a plain `for` is clearer and equivalent.
- **`in` is linear** — build a `set` if you probe membership often.
