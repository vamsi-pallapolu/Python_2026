# Data Types

Source: `Basics/5_datatypes.py`

## What is a data type?
A data type tells Python **what kind of value** something is — a number, text, a list, `True`/`False`, etc. Python figures out the type automatically from the value; you can check it with `type(x)`.

## Categories
| Category | Types |
|----------|-------|
| Numeric  | `int`, `float`, `complex`, `bool` |
| Sequence | `str`, `list`, `tuple`, `range` |
| Set      | `set`, `frozenset` |
| Mapping  | `dict` |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| None     | `NoneType` |

## Mutable vs immutable
- **Immutable:** `int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `bytes`.
- **Mutable:** `list`, `dict`, `set`, `bytearray`.

## List — ordered, mutable, allows duplicates
```python
l1 = ['apple', 1, 3.4]
l1[1] = 5                     # supports item assignment
```

## Tuple — ordered, immutable
```python
t = (1, 2, 3)
# t[1] = 4    # TypeError
```

## Set — unordered, unique, mutable
```python
chars = {'a', 'b', 'b', 'c'}   # {'a', 'b', 'c'}
# chars[0]                     # TypeError (not subscriptable)
```

## Dict — key → value mapping
```python
numbers = {1: 'One', 2: 'two'}
for k in numbers:
    print(numbers[k])
```

## Special float values
```python
import math
math.nan
float('inf')
float('-inf')
```

## Type conversion (casting)
```python
int("10")       # 10
float("3.14")   # 3.14
str(42)         # "42"
list("abc")     # ['a', 'b', 'c']
tuple([1, 2])   # (1, 2)
set("aab")      # {'a', 'b'}
```

Convert `int` → `str` — three ways:
```python
str(n)             # method 1
f"{n}"             # method 2
"{}".format(n)     # method 3
```

## Safe conversion
```python
try:
    n = int(s)
except ValueError:
    print(f"Invalid input {s!r}, cannot convert to integer")

if s.isdigit():
    n = int(s)
else:
    print("The string is not numeric")
```

## Random numbers
```python
import random
random.randint(1, 5)      # inclusive on both ends
random.uniform(1, 10)     # float in [1, 10]  (upper bound may be excluded due to FP rounding)
random.choice([1, 2, 3])  # pick one
random.shuffle(lst)       # in-place shuffle
```

## Inspecting types
```python
type(x)                  # exact type
isinstance(x, int)       # preferred (subclass-aware) type check
```
