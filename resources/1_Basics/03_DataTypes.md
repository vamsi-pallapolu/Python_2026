# Data Types

Source: `src/1_Basics/5_datatypes.py`

## Definition
A data type describes what kind of value an object holds and what operations it supports.

Python is dynamically typed, so a variable name can refer to objects of different types over time.

## Lists
A `list` is an ordered, mutable collection.
```python
l1 = ["apple", 1, 3.4]
print(l1)

l1[1] = 5
print(l1)
```

Lists support indexing and item assignment.

## Tuples
A `tuple` is an ordered, immutable collection.
```python
t = (1, 2, 3)
print(t[1])        # 2
```

This is not allowed:
```python
t[1] = 4           # TypeError
```

Use tuples for fixed collections that should not be changed element by element.

## Sets
A `set` stores unique, unordered elements.
```python
chars = {"a", "b", "b", "c"}

for char in chars:
    print(char)
```

Duplicate values are removed.

Sets do not support indexing:
```python
chars[1]           # TypeError
```

## Dictionaries
A `dict` stores key-value pairs.
```python
numbers = {1: "One", 2: "two"}

for number in numbers:
    print(numbers[number])
```

Iterating over a dictionary directly gives keys.

## Random numbers
The `random` module provides functions for random values.
```python
import random

random.randint(1, 5)       # integer from 1 through 5
random.uniform(1, 10)      # float from 1 through 10
```

## Special float values
```python
import math

print(math.nan)
print(float("inf"))
print(float("-inf"))
```

| Value | Meaning |
|-------|---------|
| `math.nan` | not a number |
| `float("inf")` | positive infinity |
| `float("-inf")` | negative infinity |

## Converting numbers to strings
```python
n = 4
s = str(n)

m = 2
s2 = f"{m}"

o = 3
s3 = "{}".format(o)
```

Prefer `str(value)` for plain conversion and f-strings when building larger messages.

## Converting strings to integers
```python
s = "123"
n = int(s)
```

Invalid input raises `ValueError`.
```python
try:
    s = "hello"
    n = int(s)
except ValueError:
    print(f'Invalid input "{s}", cannot convert to integer')
```

Use `.isdigit()` before converting simple positive integer strings.
```python
s1 = "hi"

if s1.isdigit():
    n = int(s1)
else:
    print("The string is not numeric")
```

## Common types
| Type | Example | Mutable? |
|------|---------|----------|
| `int` | `10` | No |
| `float` | `3.14` | No |
| `str` | `"hello"` | No |
| `list` | `[1, 2, 3]` | Yes |
| `tuple` | `(1, 2, 3)` | No |
| `set` | `{1, 2, 3}` | Yes |
| `dict` | `{"a": 1}` | Yes |

## Gotchas
- **Lists are mutable** - item assignment works.
- **Tuples are immutable** - item assignment raises `TypeError`.
- **Sets are unordered** - do not rely on printed order.
- **Dictionaries iterate over keys by default**.
- **`int("hello")` raises `ValueError`**.
- **`isdigit()` is useful but limited** - it does not handle negatives or decimals.
