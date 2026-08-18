# Tuples

Source: `DataStructures/3_tuples.py`

## What is a tuple?
A tuple is an **immutable, ordered sequence** of items. Like lists, tuples support indexing, slicing, iteration, and can hold mixed types — but once created, their contents cannot be changed (no `append`, `remove`, or item assignment). Immutability makes tuples hashable, so they can be used as dictionary keys or set elements — provided every element inside is itself hashable.

## Creating a tuple
```python
t = ()                  # empty tuple
t = ('hello', 'world')  # literal
t = tuple('Geek')       # from any iterable → ('G', 'e', 'e', 'k')
```

**Single-element tuple** — the trailing comma is required. Without it, the parentheses are just grouping.
```python
t = (10,)       # tuple
type(t)         # <class 'tuple'>

x = (10)        # int — parentheses only, no comma
```

## Accessing elements
Zero-based indexing and slicing, identical to lists / strings.
```python
t = (1, 2, 3, 4)
t[0]        # 1
t[1:len(t)] # (2, 3, 4)
t[:4]       # (1, 2, 3, 4)
```
Slicing returns a **new tuple**.

## Tuple packing
Comma-separated values on the right of `=` are packed into a tuple automatically — parentheses are optional.
```python
a = 1, 'hello', True
a           # (1, 'hello', True)
```

## Tuple unpacking
Assign each element to its own name in one step. Names count must match the tuple length (unless using `*`).
```python
t = ('Geek', 'for', 'geeks')
word1, word2, word3 = t
```

**Starred unpacking** — `*name` collects the "middle" or "rest" of the items into a **list**.
```python
a, *b, c = (1, 2, 3, 4, 5)
a           # 1
b           # [2, 3, 4]  ← list, not tuple
c           # 5
```

## Concatenation
`+` returns a new tuple; the originals are unchanged (tuples are immutable).
```python
tuple1 = (1, 2, 3)
tuple2 = ('hi', 'hello', 'world')
tuple3 = tuple1 + tuple2
# (1, 2, 3, 'hi', 'hello', 'world')
```

## Count and index
The only two methods tuples have — everything else is a builtin or an operator.
```python
(1, 1, 2, 2, 3, 4, 4).count(1)      # 2
(1, 2, 3, 4, 5).index(3)            # 2  → first index of value 3
```
`index` raises `ValueError` if the value is missing.

## Deleting a tuple
You cannot delete an item from a tuple, but you can delete the whole name binding.
```python
tuple1 = (1, 2, 3, 4, 5)
del tuple1
# tuple1        # NameError: name 'tuple1' is not defined
```

## Reversing a tuple
```python
t = (1, 2, 3, 4, 5)

t[::-1]                     # (5, 4, 3, 2, 1)   — slice with step -1
tuple(reversed(t))          # (5, 4, 3, 2, 1)   — reversed() returns an iterator
list(reversed(t))           # [5, 4, 3, 2, 1]

# Manual loop
for i in range(len(t) - 1, -1, -1):
    print(t[i])

# Generator expression → new tuple
tuple(t[i] for i in range(len(t) - 1, -1, -1))
```

## Tuples ↔ dict
A list of `(key, value)` tuples is the standard shape for building a dict.
```python
l = [(1, "one"), (2, "two")]

# Using dict()
d = dict(l)                             # {1: 'one', 2: 'two'}

# Using a dict comprehension
res = {key: value for key, value in l}

# Using a for loop
d = {}
for key, value in l:
    d[key] = value
```
The reverse — `dict.items()` — yields `(key, value)` tuples, so this pairing is common when iterating dicts.

## Common operations
| Operation | Effect |
|-----------|--------|
| `len(t)` | number of elements |
| `t[i]` / `t[i:j]` | index / slice (new tuple) |
| `t + u` | concatenation (new tuple) |
| `t * n` | repetition (new tuple) |
| `x in t` / `x not in t` | membership |
| `t.count(x)` | count occurrences of `x` |
| `t.index(x)` | first index of `x` (raises `ValueError` if missing) |
| `min(t)` / `max(t)` / `sum(t)` | builtins over the tuple |
| `sorted(t)` | returns a **list**, not a tuple |
| `reversed(t)` | iterator (wrap in `tuple(...)` or `list(...)`) |
| `del t` | delete the whole binding |

## Tuple vs list — when to use which
- Use a **tuple** for a fixed, meaningful record (e.g. `(x, y)` coordinates, a row from a query, a return value with multiple parts).
- Use a **list** when the collection will grow, shrink, or be reordered.
- Tuples are hashable (if all elements are), so they work as dict keys / set members; lists don't.

## Gotchas
- **`(10)` is not a tuple** — it's just `10`. Use `(10,)` for a one-element tuple.
- **Immutability is shallow** — a tuple containing a list still lets you mutate that inner list: `t = ([1, 2],); t[0].append(3)` works. The tuple's *references* are frozen, not the objects they point to. This also means such a tuple is **not** hashable.
- **`sorted(t)` returns a list** — wrap in `tuple(...)` if you need a tuple back.
- **Starred unpacking yields a list, not a tuple** — `a, *b, c = (1,2,3,4,5)` gives `b == [2, 3, 4]`.
- **Trailing comma is significant** — `1,` is a one-element tuple; `1` is an int. Parentheses are just grouping.
