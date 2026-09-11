# Comments and Docstrings

## Definition
A comment is text in your code that Python ignores.

A docstring is a string that documents a module, function, class, or method.

Comments are mainly for people reading the code.

Docstrings can also be read by tools such as `help()`.

## Line Comments
Use `#` for comments.

```python
# This is a comment
age = 25

print(age)  # This is an inline comment
```

Python ignores everything after `#` on that line, unless the `#` is inside a string.

```python
message = "This # is part of the string"
```

## Good Comments
Good comments explain why something is done.

```python
# Use a timeout so the program does not wait forever.
response = fetch_data(timeout=10)
```

Avoid comments that repeat the code.

```python
# Add 1 to count
count = count + 1
```

The code already says that.

## Multi-Line Comments
Python does not have a special block comment syntax.

Use several `#` lines.

```python
# This section validates user input before saving.
# Invalid records are skipped and reported later.
```

Do not use triple-quoted strings as comments. They are strings, not real comments.

## Docstrings
A docstring is the first statement inside a module, function, class, or method.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

You can view the docstring with `help()`.

```python
help(add)
```

You can also access it with `.__doc__`.

```python
print(add.__doc__)
```

## Function Docstrings
A short function can use a one-line docstring.

```python
def square(number):
    """Return number multiplied by itself."""
    return number * number
```

A longer function can use a multi-line docstring.

```python
def divide(a, b):
    """Return a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b
```

## Module Docstrings
A module docstring appears at the top of a file.

```python
"""Utilities for formatting user names."""

def format_name(first, last):
    return f"{first} {last}"
```

## Class Docstrings
A class docstring explains what the class represents.

```python
class User:
    """Represent a user account."""

    def __init__(self, name):
        self.name = name
```

## Tool Comments
Some comments are read by tools even though Python itself ignores them.

```python
#!/usr/bin/env python3
# type: ignore
# noqa: F401
```

These should be used only when needed.

## Common Mistakes
- Writing comments that only repeat the code.
- Forgetting that a docstring must be the first statement.
- Using triple-quoted strings as normal comments.
- Leaving outdated comments after changing code.
- Writing too many comments instead of clearer code.

## Summary
- Use `#` for comments.
- Comments should explain why, not repeat what.
- Use docstrings to document modules, functions, classes, and methods.
- `help()` can show docstrings.
