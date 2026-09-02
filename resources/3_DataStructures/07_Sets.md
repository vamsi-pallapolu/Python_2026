# Sets

Source: `DataStructures/5_0_set.py`, `5_1_setmethods.py`, `5_2_builtinOnSets.py`

## Definition
A `set` is a **mutable, unordered collection of unique hashable elements**.

Sets are useful for:
- removing duplicates
- fast membership tests
- mathematical set operations like union and intersection

## Creation
```python
s = {1, 2, 3, 4, 5, 5}
print(s)                 # {1, 2, 3, 4, 5}

empty = set()            # empty set
not_a_set = {}           # empty dict
```

Use `set(iterable)` to build a set from another collection:
```python
letters = set("hello")
print(letters)           # {'h', 'e', 'l', 'o'}
```

## Accessing and iteration
Sets are unordered and do not support indexing.
```python
s = {1, 2, 3}

for item in s:
    print(item)

s[0]                     # TypeError: 'set' object is not subscriptable
```

If sorted output is needed, use `sorted(s)`, which returns a list.
```python
s = {3, 1, 2}
sorted_s = sorted(s)     # [1, 2, 3]
```

## Adding elements
| Method | Effect |
|--------|--------|
| `s.add(x)` | add one element |
| `s.update(iterable)` | add every element from an iterable |

```python
s = {1, 2, 3}
s.add(4)
print(s)                 # {1, 2, 3, 4}

s.update([4, 5, 5])
print(s)                 # {1, 2, 3, 4, 5}
```

Duplicates are ignored because a set stores only unique elements.

## Removing elements
| Method | Effect |
|--------|--------|
| `s.remove(x)` | remove `x`; raises `KeyError` if missing |
| `s.discard(x)` | remove `x` if present; no error if missing |
| `s.pop()` | remove and return an arbitrary element; raises `KeyError` if empty |
| `s.clear()` | remove all elements |

```python
s = {1, 2, 3, 4, 5}

s.remove(5)              # ok
s.discard(6)             # no error
item = s.pop()           # arbitrary item
s.clear()                # set()
```

Use `discard()` when it is acceptable for the element to be absent.

## Membership
```python
s = {1, 2, 3}

2 in s                   # True
9 not in s               # True
```

Membership checks are one of the main reasons to use sets.

## Set operations
| Operation | Method | Operator | Result |
|-----------|--------|----------|--------|
| Union | `s1.union(s2)` | `s1 | s2` | all elements from both sets |
| Intersection | `s1.intersection(s2)` | `s1 & s2` | elements common to both |
| Difference | `s1.difference(s2)` | `s1 - s2` | elements in `s1` but not `s2` |
| Symmetric difference | `s1.symmetric_difference(s2)` | `s1 ^ s2` | elements in either set, but not both |

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.union(s2)                    # {1, 2, 3, 4}
s1.intersection(s2)             # {2, 3}
s1.difference(s2)               # {1}
s1.symmetric_difference(s2)     # {1, 4}
```

These methods return new sets and do not change the original sets.

## Update operations
Update methods mutate the left-hand set in place.
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1.intersection_update(s2)      # s1 becomes {2, 3}
```

| Method | Operator form | Effect on `s1` |
|--------|---------------|----------------|
| `s1.update(s2)` | `s1 |= s2` | keep all elements from both |
| `s1.intersection_update(s2)` | `s1 &= s2` | keep only common elements |
| `s1.difference_update(s2)` | `s1 -= s2` | remove elements found in `s2` |
| `s1.symmetric_difference_update(s2)` | `s1 ^= s2` | keep elements in either set, but not both |

Mutating methods return `None`.

## Relationship checks
| Method | Meaning |
|--------|---------|
| `s1.isdisjoint(s2)` | no common elements |
| `s1.issubset(s2)` | every element of `s1` is in `s2` |
| `s1.issuperset(s2)` | every element of `s2` is in `s1` |

```python
{1, 2, 3}.isdisjoint({4, 5})     # True
{1, 2}.issubset({1, 2, 3})       # True
{1, 2, 3}.issuperset({1, 2})     # True
```

Operator forms:
```python
{1, 2} <= {1, 2, 3}              # subset
{1, 2, 3} >= {1, 2}              # superset
{1, 2} < {1, 2, 3}               # proper subset
```

## Built-ins on sets
| Call | Result |
|------|--------|
| `len(s)` | number of unique elements |
| `min(s)` / `max(s)` | smallest / largest comparable element |
| `sorted(s)` | sorted list |
| `sum(s)` | sum of numeric elements |
| `any(s)` / `all(s)` | boolean reductions |

```python
s = {3, 1, 2}

min(s)                 # 1
max(s)                 # 3
sorted(s)              # [1, 2, 3]
```

## Finding min and max manually
```python
s = {3, 1, 2}

min_value = float("inf")
max_value = float("-inf")

for value in s:
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value

print(min_value, max_value)       # 1 3
```

## Frozensets
A `frozenset` is an immutable set. It can be used as a dictionary key or as an element inside another set.
```python
fs = frozenset([1, 2, 3])

hash(fs)                          # ok
{fs, frozenset([3, 4])}
```

Use `set` when the collection needs to change. Use `frozenset` when the set must be immutable or hashable.

## Complexity
| Operation | Average cost |
|-----------|--------------|
| `x in s` | O(1) |
| `s.add(x)`, `s.remove(x)`, `s.discard(x)` | O(1) |
| `len(s)` | O(1) |
| Iteration | O(n) |
| `s1 | s2`, `s1 & s2`, `s1 - s2` | O(len(s1) + len(s2)) |
| `sorted(s)` | O(n log n) |

Set operations are hash-table based, so O(1) operations are average-case.

## Gotchas
- **Sets are unordered** — iteration order is not a reliable program behavior.
- **No indexing or slicing** — use a list or tuple when position matters.
- **`{}` is an empty dict** — use `set()` for an empty set.
- **Elements must be hashable** — lists, dictionaries, and sets cannot be set elements.
- **`remove()` raises on missing values** — use `discard()` when missing is acceptable.
- **`pop()` removes an arbitrary element** — do not use it when you need a specific value.
- **Mutating methods return `None`** — do not assign the result of `update()` or `intersection_update()`.
