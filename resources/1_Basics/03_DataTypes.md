# Data Types

Source: `src/1_Basics/5_datatypes.py`

## Definition
A data type describes what kind of value something is and what operations it supports.

```python
age = 25
name = "Vamsi"
price = 19.99
```

Python is dynamically typed, so the variable name does not need a declared type.

## Common Built-in Types
| Type | Example | Meaning |
|------|---------|---------|
| `int` | `10` | whole number |
| `float` | `3.14` | decimal number |
| `str` | `"hello"` | text |
| `bool` | `True` | true or false |
| `list` | `[1, 2, 3]` | ordered, changeable collection |
| `tuple` | `(1, 2, 3)` | ordered, unchangeable collection |
| `set` | `{1, 2, 3}` | unique unordered values |
| `dict` | `{"name": "Vamsi"}` | key-value pairs |
| `NoneType` | `None` | no value |

## Numbers
Integers store whole numbers.

```python
count = 10
```

Floats store decimal numbers.

```python
price = 19.99
```

Basic math works with both:

```python
print(10 + 5)
print(10 / 4)
```

## Strings
A string stores text.

```python
name = "Python"
message = 'Hello'
```

Strings are ordered, so you can access characters by index.

```python
word = "Python"
print(word[0])
print(word[-1])
```

Output:

```text
P
n
```

Strings are immutable. You cannot change one character in place.

## Lists
A list is an ordered, mutable collection.

```python
items = ["apple", "banana", "orange"]

print(items[0])
items[1] = "grape"
print(items)
```

Lists are useful when you need to add, remove, or change items.

## Tuples
A tuple is ordered but immutable.

```python
point = (10, 20)

print(point[0])
```

This is not allowed:

```python
point[0] = 99  # TypeError
```

Use tuples for fixed groups of values.

## Sets
A set stores unique values.

```python
colors = {"red", "blue", "red"}
print(colors)
```

The duplicate `"red"` is stored only once.

Sets are unordered, so do not use indexes with them.

## Dictionaries
A dictionary stores key-value pairs.

```python
person = {
    "name": "Vamsi",
    "age": 25,
}

print(person["name"])
```

Use dictionaries when each value has a label.

## Type Conversion
Convert values with functions such as `str()`, `int()`, and `float()`.

```python
age_text = "25"
age = int(age_text)

print(age + 1)
```

Invalid conversion raises `ValueError`.

```python
int("hello")  # ValueError
```

## Checking Types
Use `type()` to see the exact type.

```python
print(type(10))
print(type("hello"))
```

Use `isinstance()` to check whether a value belongs to a type.

```python
value = 10

if isinstance(value, int):
    print("integer")
```

## Common Mistakes
- Trying to change a tuple or string in place.
- Expecting sets to keep a reliable order.
- Forgetting that dictionary lookup by a missing key raises `KeyError`.
- Converting invalid text with `int()` or `float()`.
- Confusing the string `"10"` with the number `10`.

## Summary
- Every value in Python has a type.
- Common types include numbers, strings, lists, tuples, sets, dictionaries, booleans, and `None`.
- Lists and dictionaries are mutable.
- Strings and tuples are immutable.
- Use conversion functions when you need a different type.
