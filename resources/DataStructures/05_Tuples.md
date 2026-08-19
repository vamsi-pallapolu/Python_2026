# Tuples

Source: `DataStructures/3_tuples.py`

## Definition
A tuple is an **immutable, ordered sequence**. Once created, its elements cannot be added, removed, or replaced. A tuple is **hashable** only when every element it holds is hashable — which makes tuples valid dict keys and set members, unlike lists.

## Creation
```python
()                      # empty tuple
(1,)                    # one-element — trailing comma is required
(1, 2, 3)               # literal
1, 2, 3                 # parentheses are optional
tuple("Geek")           # from any iterable → ('G', 'e', 'e', 'k')
```
The **comma** builds the tuple; parentheses only group. `(10)` is the int `10`; `(10,)` is a one-element tuple.

## Indexing, slicing, and operators
Same protocol as lists and strings. Each operation returns a **new tuple** — the original is untouched.
```python
t = (1, 2, 3, 4)
t[0]                    # 1
t[-1]                   # 4
t[1:3]                  # (2, 3)
t + (5, 6)              # (1, 2, 3, 4, 5, 6)
t * 2                   # (1, 2, 3, 4, 1, 2, 3, 4)
3 in t                  # True
```

## Packing and unpacking
Right-hand-side commas pack; left-hand-side names unpack. Counts must match.
```python
a = 1, "hello", True                # packing → (1, "hello", True)
x, y, z = (10, 20, 30)              # unpacking
x, y = y, x                         # swap without a temp
```

**Starred unpacking** collects the middle or the ends into a **list** (not a tuple):
```python
a, *b, c = (1, 2, 3, 4, 5)
# a == 1, b == [2, 3, 4], c == 5
```

## Methods
Tuples expose only two methods; everything else is a builtin or an operator.
```python
(1, 1, 2, 3).count(1)               # 2
(1, 2, 3, 4).index(3)               # 2 — first index of value 3
```
`index` raises `ValueError` if the value is missing.

## Builtins on tuples
| Call | Result |
|------|--------|
| `len(t)` | length |
| `min(t)` / `max(t)` / `sum(t)` | reductions |
| `sorted(t)` | **list** (not a tuple) |
| `reversed(t)` | iterator — wrap in `tuple(...)` or `list(...)` |
| `any(t)` / `all(t)` | boolean reductions |

## Deleting
An element cannot be removed. The whole binding can:
```python
t = (1, 2, 3)
del t                   # `t` is now unbound
```

## Tuples ↔ dict
`dict.items()` yields `(key, value)` tuples, and `dict()` accepts a sequence of `(key, value)` pairs. That symmetry is why tuples show up whenever dicts are constructed or iterated.
```python
pairs = [(1, "one"), (2, "two")]
dict(pairs)                                 # {1: 'one', 2: 'two'}
{k: v for k, v in pairs}                    # same result
```

## Named tuples and frozen dataclasses
For structured records with field names, prefer one of these over positional tuples:
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x, p.y                # 1, 2 — still indexable and unpackable

from typing import NamedTuple
class Point(NamedTuple):
    x: int
    y: int              # typed variant

from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
    x: int
    y: int              # immutable + hashable, richer than NamedTuple
```

## When to use a tuple
- Fixed **heterogeneous** records — coordinates, a database row, multi-value return.
- **Dict keys** or **set members** — need hashability.
- Constants that must not be reassigned element-wise.

Use a **list** when the collection will grow, shrink, or be reordered.

## Hashability rule
A tuple is hashable only when **every element** is hashable.
```python
hash((1, 2, "x"))                   # ok
hash((1, [2, 3]))                   # TypeError — inner list is unhashable
```

## Gotchas
- **`(10)` is not a tuple** — parentheses without a comma are grouping. Use `(10,)`.
- **Immutability is shallow** — a tuple's references are frozen; the objects they point at are not. `t = ([1, 2],); t[0].append(3)` succeeds. Such a tuple is also **not hashable**.
- **`sorted(t)` returns a list.** Wrap in `tuple(...)` for a tuple.
- **Starred unpacking yields a list**, not a tuple: `a, *b = (1, 2, 3)` gives `b == [2, 3]`.
- **`t.index(x)` raises on miss** — guard with `x in t` if the value may be absent.
