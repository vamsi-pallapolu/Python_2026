# Python Data Structure Methods — Practiced So Far

A single reference of every operation, method, and built-in used across the practice files for **Strings, Lists, Tuples, Dictionaries, Sets, and Frozensets**. Grouped by data structure and by purpose.

Source files:
- `DataStructures/1_string.py`
- `DataStructures/2_0_list.py`, `2_1_iteration.py`, `2_2_2d.py`
- `DataStructures/3_tuples.py`
- `DataStructures/4_0_dict.py`, `4_1_iteration.py`, `4_2_comprehension.py`, `4_3_dictmethods.py`
- `DataStructures/5_0_set.py`, `5_1_setmethods.py`, `5_2_builtinOnSets.py`

---

# 1. Strings (`str`)

Ordered, **immutable** sequence of characters. Every "change" returns a brand-new string.

## Built-ins that work on strings
| Call | What it does | Example |
|------|--------------|---------|
| `len(s)` | Number of characters | `len("Vamsi") → 5` |
| `str(x)` | Convert any value to a string | `str(123) → '123'` |
| `list(s)` | Break the string into a list of single characters | `list("Py") → ['P','y']` |
| `id(s)` | Memory identity — useful for proving immutability | `id(s)` differs after `s = 'A' + s[1:]` |
| `del s` | Unbinds the name; using `s` afterwards raises `NameError` | `del s` |

## Indexing and slicing
| Form | Meaning | Example |
|------|---------|---------|
| `s[i]` | Character at position `i` (0-based) | `"abc"[1] → 'b'` |
| `s[-i]` | Count from the end | `"abc"[-1] → 'c'` |
| `s[a:b]` | Substring from `a` up to (not including) `b` | `"abcdef"[1:4] → 'bcd'` |
| `s[:b]` / `s[a:]` | From start / to end | `"abcdef"[:3] → 'abc'` |
| `s[::-1]` | Reverse the string | `"abc"[::-1] → 'cba'` |
| `s[::k]` | Every `k`-th character | `"abcdef"[::2] → 'ace'` |

## Methods
| Method | What it does | Example |
|--------|--------------|---------|
| `s.upper()` | Every letter to uppercase | `"hello".upper() → 'HELLO'` |
| `s.lower()` | Every letter to lowercase | `"LOWeR".lower() → 'lower'` |
| `s.strip()` / `s.lstrip()` / `s.rstrip()` | Remove whitespace from both / left / right | `"  hi  ".strip() → 'hi'` |
| `s.replace(old, new)` | Replace every `old` with `new` | `"fun".replace("fun","cool")` |
| `s.split()` | Split on any run of whitespace | `"a b".split() → ['a','b']` |
| `s.split(sep)` | Split on a specific delimiter | `"1,2".split(',') → ['1','2']` |
| `s.startswith(x)` / `s.endswith(x)` | Prefix / suffix check | `"hello dude".startswith("hello") → True` |
| `s.isdigit()` | All characters are digits | `"123".isdigit() → True` |
| `s.isalpha()` | All characters are letters | `"abc".isalpha() → True` |
| `s.format(...)` | Older placeholder-style formatting | `"{},{}".format(a,b)` |

## Operators
| Op | Meaning | Example |
|----|---------|---------|
| `+` | Concatenate | `"a"+"b" → 'ab'` |
| `*` | Repeat | `"Hi "*3 → 'Hi Hi Hi '` |
| `in` | Substring membership | `"Hello" in "Hello World" → True` |
| `==` | Value equality | `"Py" == "Py" → True` |
| `is` | Same object in memory — do not rely on it for text equality | `s1 is s2` |

## Formatting
```python
name, age = "Vamsi", 29
f"name is {name}, age is {age}"       # f-string (preferred)
"name: {}, age: {}".format(name, age) # str.format
```

---

# 2. Lists (`list`)

Ordered, **mutable** sequence. Can hold any mix of types.

## Creation
```python
a = [1, 2, 3]
b = list((4, 5, 6))
c = [1] * 3          # [1, 1, 1]
```

## Access
| Form | Meaning |
|------|---------|
| `a[i]` | Item at index `i` |
| `a[-1]` | Last item |
| `a[a:b]` | Slice (same rules as strings) |
| `a[i][j]` | Nested access (2D list) |

## Adding items
| Method | What it does | Example |
|--------|--------------|---------|
| `a.append(x)` | Add one item to the end | `a.append(4)` |
| `a.insert(i, x)` | Insert at position `i`, shifts others right | `a.insert(1, 2)` |
| `a.extend(iterable)` | Append every item from another iterable | `a.extend([10, 20])` |

## Updating
```python
a[1] = 10   # direct assignment works — lists are mutable
```

## Removing items
| Method | What it does | Example / Behavior |
|--------|--------------|--------------------|
| `a.remove(x)` | Remove first occurrence of value `x` | Raises `ValueError` if absent |
| `del a[i]` / `del a[a:b]` | Delete by index or slice | In-place |
| `a.clear()` | Empty the list | `a → []` |

## Iteration
```python
for item in a: ...
for i, item in enumerate(a): ...
for i in range(len(a)): print(a[i])
while index < len(a): ...
```

## Multi-dimensional (2D) lists
```python
mat = [[1, 2, 3], [4, 5, 6]]

for row in mat:                       # row-by-row
    print(row)

for i in range(len(mat)):             # index-based
    for j in range(len(mat[i])):
        print(mat[i][j])

for i, row in enumerate(mat):         # enumerate-based
    for j, value in enumerate(row):
        print(value)

mat[0].reverse()                      # reverse a row in place
mat.reverse()                         # reverse the outer list
```

## Building an m×n zero matrix
```python
m, n = 4, 5
mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)
```

## List comprehensions
```python
double = [x*2 for x in [1,2,3]]                  # transform
evens  = [n for n in nums if n % 2 == 0]         # filter
labels = ["EVEN" if n%2==0 else "ODD" for n in nums]  # if/else

pairs = [(x, y) for x in range(3) for y in range(3)]        # nested loop
flat  = [x for row in mat for x in row]                     # flatten
double_mat = [[x*2 for x in row] for row in mat]            # 2D transform
```

---

# 3. Tuples (`tuple`)

Ordered, **immutable** sequence. Once created it cannot be changed.

## Creation
```python
t = ()                # empty tuple
t = ('hello', 'world')
t = tuple('Geek')     # ('G','e','e','k')
t = (10,)             # single-element tuple — the comma is required
```

## Access
```python
t = (1, 2, 3, 4)
t[0]        # 1
t[1:3]      # (2, 3)      slicing works like lists/strings
t[::-1]     # reversed copy
```

## Packing and unpacking
```python
a = 1, 'hi', True             # packing → (1, 'hi', True)
w1, w2, w3 = ('a', 'b', 'c')  # unpacking
a, *b, c = (1, 2, 3, 4, 5)    # a=1, b=[2,3,4], c=5   (star grabs the middle)
```

## Concatenation
```python
(1, 2) + (3, 4)     # (1, 2, 3, 4)
```

## Methods (tuples only have two)
| Method | What it does | Example |
|--------|--------------|---------|
| `t.count(x)` | How many times `x` appears | `(1,1,2).count(1) → 2` |
| `t.index(x)` | First position of `x` (raises `ValueError` if absent) | `(1,2,3).index(3) → 2` |

## Deleting
```python
del t          # unbinds the whole tuple
# del t[0]     # TypeError — tuples are immutable
```

## Reversing
```python
t[::-1]                # slice — new tuple
tuple(reversed(t))     # reversed() iterator → tuple
list(reversed(t))      # or into a list
```

## Tuples → dict
```python
pairs = [(1, "one"), (2, "two")]

dict(pairs)                        # dict constructor
{k: v for k, v in pairs}           # comprehension
d = {}
for k, v in pairs:                 # loop
    d[k] = v
```

---

# 4. Dictionaries (`dict`)

Stores data as **key → value** pairs. Keys are unique and immutable (str, int, tuple). Values can be anything.

## Creation
```python
coords = {'x': 1, 'y': 2}
person = dict(name="vamsi", age=21)
```

## Access
```python
person['name']       # KeyError if missing
person.get('age')    # returns None if missing (safer)
```

## Adding and updating
```python
person['lastName'] = 'pallapolu'   # add
person['age'] = 31                 # update — assigning to existing key overwrites
```

## Removing
| Method | What it does | Example |
|--------|--------------|---------|
| `del d[key]` | Delete a key (raises `KeyError` if missing) | `del person['lastName']` |
| `d.pop(key)` | Remove a key and return its value | `person.pop('age')` |
| `d.popitem()` | Remove and return the last inserted (key, value) pair | `person.popitem()` |
| `d.clear()` | Empty the dictionary | `person.clear()` |

## Update and setdefault
| Method | What it does | Example |
|--------|--------------|---------|
| `d.update(other)` | Merge another dict/pairs in — overwrites duplicate keys | `d.update({'b':4,'c':3})` |
| `d.setdefault(k, v)` | Return `d[k]` if present; otherwise set it to `v` and return `v` | `d.setdefault('c', 4)` |

## Iterating
```python
for key in d:               # keys (default)
for key in d.keys():        # keys (explicit)
for val in d.values():      # values
for k, v in d.items():      # both
```

## Nested dictionaries
```python
students = {
    "s1": {"name": "vamsi", "age": 18},
    "s2": {"name": "krishna", "age": 18},
}
for student, details in students.items():
    for k, v in details.items():
        print(k, v)
```

## Dictionary comprehensions
```python
{x: x*2 for x in range(1, 5)}                     # from a range
{k: v for k, v in zip(l1, l2)}                    # from two lists
{c: "Char" for c in "wor123&*" if c.isalpha()}    # with a filter
{fruit: len(fruit) for fruit in ['apple','mango']}

# Nested comprehension
{x: {y: x+y for y in "GF"} for x in "GF"}
```

## `fromkeys`
```python
dict.fromkeys(range(5), True)   # {0:True, 1:True, 2:True, 3:True, 4:True}
```

## Copying — shallow vs deep
```python
import copy
student = {"name": "Emma", "marks": [90, 85, 92]}

shallow = student.copy()          # top level copied, inner list shared
deep    = copy.deepcopy(student)  # everything copied top-to-bottom
```
Editing `shallow["marks"][0]` also changes `student["marks"][0]` — the inner list is shared. `deep` is fully independent.

---

# 5. Sets (`set`)

Unordered collection of **unique** elements. No indexing, no duplicates.

## Creation
```python
s = {1, 2, 3, 4, 5, 5, 6}    # {1, 2, 3, 4, 5, 6} — duplicates dropped
s = set()                     # empty set — NOT {} (that's an empty dict)
```

## Access
```python
for item in s:      # iteration works — but order is not guaranteed
    print(item)

s[0]                # TypeError: 'set' object is not subscriptable
```

## Adding
| Method | What it does | Example |
|--------|--------------|---------|
| `s.add(x)` | Add one element (no-op if already present) | `s.add(4)` |
| `s.update(iterable)` | Add every element from an iterable, duplicates ignored | `s.update([4, 5, 5])` |

## Removing
| Method | What it does | Missing element |
|--------|--------------|-----------------|
| `s.remove(x)` | Remove `x` | Raises `KeyError` |
| `s.discard(x)` | Remove `x` if present | Silent — no error |
| `s.pop()` | Remove and return an arbitrary element | Raises `KeyError` on empty set |
| `s.clear()` | Empty the set | — |

## Membership
```python
3 in s              # True / False
```

## Set algebra — method form (return a new set)
| Method | What it does | Example |
|--------|--------------|---------|
| `s1.union(s2)` | All elements from both — same as `s1 \| s2` | `{1,2,3}.union({2,3,4}) → {1,2,3,4}` |
| `s1.intersection(s2)` | Elements in both — same as `s1 & s2` | `{1,2,3}.intersection({2,3,4}) → {2,3}` |
| `s1.difference(s2)` | In `s1` but not in `s2` — same as `s1 - s2` | `{1,2,3}.difference({2,3,4}) → {1}` |
| `s1.symmetric_difference(s2)` | In one but not both — same as `s1 ^ s2` | `{1,2,3}.symmetric_difference({2,3,4}) → {1,4}` |

Each of these returns a **new set** and leaves `s1` unchanged.

## Set algebra — in-place `_update` versions (mutate `s1`)
| Method | What it does |
|--------|--------------|
| `s1.intersection_update(s2)` | Keep in `s1` only what's also in `s2` |
| `s1.difference_update(s2)` | Remove from `s1` everything that's in `s2` |
| `s1.symmetric_difference_update(s2)` | Keep only elements that were in one set but not both |

Naming rule: any `x_update()` method **mutates `s1` in place** and returns `None`; the same-name method without `_update` returns a new set.

## Comparison methods
| Method | What it checks | Example |
|--------|----------------|---------|
| `s1.isdisjoint(s2)` | No shared elements (`s1 ∩ s2 == ∅`) | `{1,2,3}.isdisjoint({4,5,6}) → True` |
| `s1.issubset(s2)` | Every element of `s1` is in `s2` (`s1 ⊆ s2`) | `{1,2}.issubset({1,2,3,4}) → True` |
| `s1.issuperset(s2)` | Every element of `s2` is in `s1` (`s1 ⊇ s2`) | `{1,2,3,4}.issuperset({1,2}) → True` |

All three accept any iterable — not just a set.

## Built-ins that work on sets (min / max / sorted)
Since sets are iterable, the standard aggregation functions work — but the set itself has no order.

```python
s = {3, 1, 2}

max(s)          # 3
min(s)          # 1

sorted_s = sorted(s)      # [1, 2, 3]  — returns a LIST, not a set
sorted_s[0]               # 1  — smallest
sorted_s[-1]              # 3  — largest
```

Manual min/max via loop (useful when you need both in one pass):
```python
min_v, max_v = float('inf'), float('-inf')
for v in s:
    if v < min_v: min_v = v
    if v > max_v: max_v = v
```

---

# 6. Frozensets (`frozenset`)

The **immutable** version of a set. Once built it cannot be added to or removed from — so it can itself be used as a dict key or as an element of another set.

## Creation
```python
fs = frozenset([1, 2, 3, 3])     # frozenset({1, 2, 3})
fs = frozenset("abc")             # frozenset({'a','b','c'})
```

## What works
- All the **read-only** operations of a set:
  - `len(fs)`, `x in fs`, iteration `for x in fs: ...`
  - Set algebra: `fs | other`, `fs & other`, `fs - other`, `fs ^ other`
  - Comparisons: `fs.issubset(other)`, `fs.issuperset(other)`, `fs.isdisjoint(other)`

## What does NOT work
- `add`, `update`, `remove`, `discard`, `pop`, `clear` — all raise `AttributeError`.
- `fs[0]` — same as sets, not subscriptable.

## When to use it
- As a dictionary key: `{frozenset({'a','b'}): "value"}`
- As a member of another set (regular sets can't hold regular sets).
- To signal "this collection must never change".

---

# Cross-structure cheat sheet

| Property | str | list | tuple | dict | set | frozenset |
|---------|:---:|:----:|:-----:|:----:|:---:|:---------:|
| Ordered | yes | yes | yes | yes (insertion order) | no | no |
| Mutable | no | yes | no | yes | yes | no |
| Allows duplicates | yes | yes | yes | keys no / values yes | no | no |
| Indexable `[i]` | yes | yes | yes | by key | no | no |
| Iterable | yes | yes | yes | yes (keys) | yes | yes |
| Can be a dict key | yes | no | yes (if items are hashable) | no | no | yes |

## Gotchas already met in practice
- **Strings are immutable** — rebuild with slicing, don't assign to `s[0]`.
- **`split()` vs `split(" ")`** — no argument drops empties; `" "` keeps them.
- **Loop concatenation `+=` on strings** is quadratic; prefer `"".join(parts)`.
- **`{}` is an empty dict, not an empty set** — use `set()`.
- **Sets are unordered** — never index a set or trust iteration order.
- **`remove` vs `discard`** — `remove` raises when missing, `discard` is silent.
- **Shallow copy of a dict** shares its inner mutable values; use `copy.deepcopy` when you need a fully independent copy.
- **`tuple(10)` is not a tuple** — you need `(10,)` (the comma is what makes it a tuple).
- **`dict.get(k)` vs `d[k]`** — `get` returns `None` on missing key, indexing raises `KeyError`.

---

# Patterns for remembering these methods

Instead of memorizing each structure separately, notice that most methods repeat across them with the **same name and the same idea**. Grouping by intent makes them stick.

## 1. The "add one" family
| Method | Where | Adds |
|--------|-------|------|
| `.append(x)` | list | one item to the end |
| `.add(x)` | set | one item (no-op if present) |

Mnemonic: sequences *append*, sets *add*.

## 2. The "add many" family
| Method | Where | Merges from |
|--------|-------|-------------|
| `.extend(iterable)` | list | any iterable |
| `.update(iterable)` | set | any iterable |
| `.update(other)` | dict | another dict / pairs |

Rule: all three take an **iterable** and merge it in.

## 3. The "insert at position"
| Method | Where |
|--------|-------|
| `.insert(i, x)` | list only |

Sets and dicts have no order → no `insert`. Strings and tuples are immutable → no `insert` either.

## 4. The "remove by value" family
| Method | Where | If missing |
|--------|-------|------------|
| `.remove(x)` | list, set | list → `ValueError`, set → `KeyError` |
| `.discard(x)` | set only | silent |

Trick: everywhere it exists, `.remove()` **raises** on missing; `.discard()` is the "safe" set-only version.

## 5. The "remove and return" family — all called `.pop()`
| Method | Where | What it returns |
|--------|-------|-----------------|
| `.pop()` / `.pop(i)` | list | last (or i-th) item |
| `.pop(key)` | dict | value for that key |
| `.pop()` | set | an arbitrary element |
| `.popitem()` | dict | last inserted `(key, value)` pair |

Rule: `pop` = remove **and** hand back what was removed.

## 6. The "empty me out" — `.clear()`
Same name everywhere: `list.clear()`, `dict.clear()`, `set.clear()`. Not on strings/tuples (immutable).

## 7. The "count me" family
| Method | Where |
|--------|-------|
| `.count(x)` | str, list, tuple |

Same idea everywhere: how many times `x` appears.

## 8. The "find first position" family
| Method | Where | If missing |
|--------|-------|------------|
| `.index(x)` | str, list, tuple | raises `ValueError` |
| `.find(x)` | str **only** | returns `-1` |

Trick: `index` raises, `find` is silent — same pattern as `remove` vs `discard`.

## 9. Built-ins that work on almost everything
These are **not methods** — they're functions that work on any iterable:

| Function | Works on |
|----------|----------|
| `len(x)` | str, list, tuple, dict, set, frozenset |
| `min(x)` / `max(x)` / `sum(x)` | str, list, tuple, set, frozenset (numbers/comparable) |
| `sorted(x)` | any iterable → returns a **list** |
| `reversed(x)` | ordered ones (str, list, tuple) |
| `any(x)` / `all(x)` | any iterable |

## 10. Operators that behave consistently
| Operator | On ordered (str, list, tuple) | On sets | On dicts |
|----------|-------------------------------|---------|----------|
| `x in c` | membership | membership | key membership |
| `+` | concatenate | not supported | not supported |
| `*` | repeat | not supported | not supported |
| `==` | element-wise equality | element-wise equality | key & value equality |

## 11. Copying — same trick everywhere
| Way | Works on |
|-----|----------|
| `.copy()` | list, dict, set |
| `copy.copy(x)` | all |
| `copy.deepcopy(x)` | all — recursively copies nested mutables |

---

## One rule that organizes the rest

Place each structure on this grid:

|                  | **Ordered**            | **Unordered**  |
|------------------|------------------------|----------------|
| **Mutable**      | list, dict\*           | set            |
| **Immutable**    | str, tuple             | frozenset      |

\*dict preserves insertion order since Python 3.7.

Then most methods fall out automatically:
- **Mutable → gets** `add/append`, `remove`, `pop`, `clear`, `update/extend`.
- **Immutable → gets** only "read" methods: `count`, `index` (+ string-only extras).
- **Ordered → supports** indexing, slicing, `reverse`, `sort`, `+`, `*`.
- **Unordered → supports** set algebra (`|`, `&`, `-`, `^`) and fast membership.

If you can place a structure on that grid, you can predict most of its methods without memorizing them individually.
