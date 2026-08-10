# Variables

Source: `Basics/2_variables.py`

## Assignment
```python
a = b = c = 20                 # same value to many names
x, y, z = "vamsi", 29, "mw"    # tuple unpacking
```

## Reference semantics
Python variables hold **references** to objects, not the values themselves.
```python
x = 1
y = x        # y refers to the same int object
y = y + 1    # y now refers to a new int; x is unchanged
```

For **mutable** objects (list, dict, set), two names can share state:
```python
a = [1, 2]
b = a
b.append(3)
print(a)   # [1, 2, 3]   — same object
```

## Identity vs equality
- `is`  — same object in memory (compares `id()`).
- `==` — same value.

```python
v1 = [1, 2, 3]
v2 = [1, 2, 3]
v1 == v2   # True
v1 is v2   # False
```

## Deleting a variable
```python
z = 30
del z          # name removed; using z now raises NameError
```

## Naming rules
- Start with a letter or `_`, followed by letters, digits, or `_`.
- Case-sensitive: `Age` and `age` are different names.
- Cannot use Python keywords (`for`, `class`, `def`, ...).
- Convention:
  - `snake_case` for variables / functions.
  - `PascalCase` for classes.
  - `UPPER_CASE` for constants.

## Practical patterns
```python
a, b = b, a                # swap without a temp
length = len("Python")     # 6
```
