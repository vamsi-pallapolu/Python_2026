# Dictionaries

Source: `DataStructures/4_0_dict.py`, `4_1_iteration.py`, `4_2_comprehension.py`, `4_3_dictmethods.py`

## Definition
A `dict` is a **mutable mapping** that stores data as key-value pairs.

- Keys must be **hashable** and unique.
- Values can be any object, including mutable objects like lists.
- In modern Python, dictionaries preserve insertion order.

## Creation
```python
coordinates = {"x": 1, "y": 2}
person = dict(name="vamsi", age=21)
empty = {}
```

Build from key-value pairs:
```python
pairs = [("one", 1), ("two", 2)]
d = dict(pairs)                 # {'one': 1, 'two': 2}
```

## Accessing values
```python
person = {"name": "vamsi", "age": 21}

person["name"]                  # 'vamsi'
person.get("age")               # 21
person.get("city")              # None
person.get("city", "unknown")   # 'unknown'
```

`d[key]` raises `KeyError` when the key is missing. `d.get(key)` returns `None` or a default value.

## Adding and updating
```python
person["lastName"] = "pallapolu"     # add new key
person["age"] = 31                   # update existing key
```

Use `update()` to merge another mapping or key-value pairs:
```python
d = {"a": 1, "b": 2}
result = d.update({"b": 4, "c": 3})

print(d)        # {'a': 1, 'b': 4, 'c': 3}
print(result)   # None
```

Mutating methods like `update()` modify the dictionary in place and return `None`.

## Removing items
| Operation | Effect |
|-----------|--------|
| `del d[key]` | remove key-value pair; raises `KeyError` if missing |
| `d.pop(key)` | remove and return value; raises `KeyError` if missing |
| `d.pop(key, default)` | remove and return value; return default if missing |
| `d.popitem()` | remove and return the last inserted key-value pair |
| `d.clear()` | remove all items |

```python
person = {"name": "vamsi", "age": 31}

age = person.pop("age")         # 31
person.clear()                  # {}
```

## Membership
Membership checks keys, not values.
```python
d = {"one": 1, "two": 2}

"one" in d          # True
1 in d              # False
1 in d.values()     # True
```

## Iteration
Iterating directly over a dictionary gives keys.
```python
d = {"one": 1, "two": 2}

for key in d:
    print(key)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(f"Key:{key},Value:{value}")
```

Use `.items()` when both the key and value are needed.

## Nested dictionaries
```python
students = {
    "student1": {"name": "vamsi", "no": 1, "age": 18},
    "student2": {"name": "krishna", "no": 2, "age": 18},
}

for student, details in students.items():
    print(f"{student} details:")
    for key, value in details.items():
        print(f"{key}:{value}")
```

## Dictionary comprehensions
Comprehensions build dictionaries from loops in one expression.
```python
doubles = {x: x * 2 for x in range(1, 5)}
# {1: 2, 2: 4, 3: 6, 4: 8}

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
lookup = {k: v for k, v in zip(letters, numbers)}
# {'a': 1, 'b': 2, 'c': 3}
```

Filtering:
```python
chars = {c: "Char" for c in "wor123&*" if c.isalpha()}
# {'w': 'Char', 'o': 'Char', 'r': 'Char'}
```

Nested dictionary comprehension:
```python
s = "GF"
d = {x: {y: x + y for y in s} for x in s}
# {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}
```

## `dict.fromkeys()`
Create a dictionary from keys with the same value.
```python
d = dict.fromkeys(range(5), True)
# {0: True, 1: True, 2: True, 3: True, 4: True}
```

Avoid using a mutable shared default:
```python
d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)
print(d)        # {'a': [1], 'b': [1]}
```

Use a comprehension when each key needs its own list:
```python
d = {key: [] for key in ["a", "b"]}
```

## `setdefault()`
`setdefault()` returns the existing value if the key exists. If the key does not exist, it inserts the default and returns it.
```python
d = {"a": 1, "b": 2}

d.setdefault("b", 3)       # 2
d.setdefault("c", 4)       # 4

print(d)                   # {'a': 1, 'b': 2, 'c': 4}
```

Common grouping pattern:
```python
groups = {}
for name in ["amy", "bob", "alex"]:
    groups.setdefault(name[0], []).append(name)

print(groups)              # {'a': ['amy', 'alex'], 'b': ['bob']}
```

## Copying
`dict.copy()` creates a shallow copy. The outer dictionary is new, but nested mutable values are shared.
```python
student = {"name": "Emma", "marks": [90, 85, 92]}
student2 = student.copy()

student2["marks"][0] = 88
print(student)             # {'name': 'Emma', 'marks': [88, 85, 92]}
```

Use `copy.deepcopy()` when nested mutable values must be independent.
```python
import copy

student = {"name": "Emma", "marks": [90, 85, 92]}
student3 = copy.deepcopy(student)

student3["marks"][0] = 88
print(student)             # {'name': 'Emma', 'marks': [90, 85, 92]}
```

## Complexity
| Operation | Average cost |
|-----------|--------------|
| `d[key]`, `d[key] = value`, `del d[key]` | O(1) |
| `key in d` | O(1) |
| `value in d.values()` | O(n) |
| `len(d)` | O(1) |
| Iteration over keys, values, or items | O(n) |
| `d.copy()` | O(n) |

Dictionary operations are hash-table based, so O(1) operations are average-case.

## Gotchas
- **Keys must be hashable** — strings, numbers, and tuples of hashable values work; lists and dictionaries do not.
- **Duplicate keys overwrite earlier values** — `{"a": 1, "a": 2}` becomes `{"a": 2}`.
- **`get()` only hides missing-key errors** — it does not distinguish a missing key from a key whose value is `None` unless you provide a custom default.
- **Membership checks keys** — use `value in d.values()` for values.
- **Mutating methods return `None`** — do not assign the result of `update()` or `clear()`.
- **Shallow copies share nested objects** — use `copy.deepcopy()` when nested data must be independent.
