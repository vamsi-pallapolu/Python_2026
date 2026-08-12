# Lists

Source: `DataStructures/2_0_list.py`

## What is a list?
A list is a **mutable, ordered, dynamic sequence** that can hold elements of any type — including mixed types. Lists are the workhorse sequence in Python: resizable, indexable, sliceable, and iterable. Because they are mutable, methods like `append`, `insert`, and `remove` modify the list **in place** and return `None`, not a new list.

## Creating a list
```python
a = [1, 2, 3]                # literal
b = list((4, 5, 6))          # from any iterable (tuple, string, range, ...)
c = [1] * 3                  # [1, 1, 1] — repetition
d = []                       # empty list
```
Note: `[obj] * n` repeats the same reference `n` times. For lists of mutable objects (e.g. `[[]] * 3`), all elements share the same inner list — use a comprehension (`[[] for _ in range(3)]`) if you need independent copies.

## Accessing elements
Zero-based indexing; negative indices count from the end.
```python
a = [1, 2, 3]
a[0]     # 1
a[-1]    # 3
```
Out-of-range access raises `IndexError`.

## Adding elements
| Method | Effect |
|--------|--------|
| `a.append(x)` | add `x` to the end (O(1) amortized) |
| `a.insert(i, x)` | insert `x` before index `i` (O(n)) |
| `a.extend(iterable)` | append each item of `iterable` (like `+=`) |

```python
a = [1, 2, 3]
a.append(4)             # [1, 2, 3, 4]
a.insert(1, 2)          # [1, 2, 2, 3, 4]
a.extend([10, 20, 30])  # [1, 2, 2, 3, 4, 10, 20, 30]
```

## Updating elements
Assign by index (unlike strings, which are immutable).
```python
a = [1, 2, 3]
a[1] = 10       # [1, 10, 3]
```

## Removing elements
| Operation | Effect |
|-----------|--------|
| `a.remove(x)` | removes the **first** occurrence of value `x` (raises `ValueError` if missing) |
| `del a[i]` | removes element at index `i` |
| `a.pop([i])` | removes and **returns** element at index `i` (default: last). Positional only — `a.pop(i=-1)` raises `TypeError`. |
| `a.clear()` | removes all elements |

```python
a = [1, 2, 3]
a.remove(2)     # [1, 3]
del a[1]        # [1]
a.clear()       # []
```

## Iterating over a list
```python
fruits = ['apple', 'banana', 'fruit']
for fruit in fruits:
    print(fruit)
```

## Nested lists
A list can hold other lists as elements — the basis for matrices / 2-D structures.
```python
a = [[1, 2, 3]]
a[0]        # [1, 2, 3]
a[0][1]     # 2
```

## List comprehension
Concise syntax to build a new list by applying an expression to each item of an iterable, optionally filtered by a condition.

**Basic form:**
```python
elements = [1, 2, 3]
double = [x * 2 for x in elements]      # [2, 4, 6]
```

**With a filter (`if`):**
```python
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]      # [2, 4]
```

**With `if / else` (ternary in the expression, not a filter):**
```python
numbers = [1, 2, 3, 4]
labels = ["EVEN" if n % 2 == 0 else "ODD" for n in numbers]
# ['ODD', 'EVEN', 'ODD', 'EVEN']
```
Note the position matters — a trailing `if` **filters**; an `if/else` in the expression **transforms**.

## More comprehension patterns
```python
# From a range
[x for x in range(5)]                       # [0, 1, 2, 3, 4]

# Nested loops (Cartesian product)
[(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), ...]

# Flattening a 2-D list
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[el for row in mat for el in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Read nested `for` clauses **left-to-right** — outer loop first, inner loop next.

## Common methods
| Method | Purpose |
|--------|---------|
| `len(a)` | number of elements |
| `a.append(x)` / `a.extend(it)` / `a.insert(i, x)` | add |
| `a.remove(x)` / `a.pop(i)` / `a.clear()` / `del a[i]` | remove |
| `a.index(x)` | first index of `x` (raises `ValueError` if missing) |
| `a.count(x)` | number of occurrences of `x` |
| `a.sort()` / `sorted(a)` | in-place vs. new sorted list |
| `a.reverse()` / `a[::-1]` | in-place reverse vs. reversed copy |
| `a.copy()` / `list(a)` / `a[:]` | shallow copy |
| `x in a` / `x not in a` | membership |
| `a + b` / `a * n` | concatenation / repetition (returns new list) |

## Slicing
Same syntax as strings — `a[start:stop:step]` — and returns a **new** list.
```python
a = [0, 1, 2, 3, 4, 5]
a[1:4]      # [1, 2, 3]
a[::-1]     # [5, 4, 3, 2, 1, 0]
a[::2]      # [0, 2, 4]
```
Slice assignment can insert, delete, or replace ranges:
```python
a[1:3] = [99]        # replaces two elements with one
```

## Gotchas
- **Mutating methods return `None`** — `a = a.append(4)` sets `a` to `None`. Chain via a temp or use `+`.
- **`list * n` shares references** — `[[]] * 3` gives three aliases of the *same* inner list; mutating one mutates all.
- **`remove` vs `del` vs `pop`** — `remove` takes a **value**, the other two take an **index**.
- **Assignment is not a copy** — `b = a` creates another name for the same list. Use `a.copy()`, `list(a)`, or `a[:]` for a shallow copy; `copy.deepcopy` for nested structures.
- **List comprehensions build the full result in memory** — use a generator expression (`(x*2 for x in xs)`) if you only need to iterate once over a large sequence.
