# Exceptions

Source: `src/1_Basics/9_0_eh.py`

## Definition
An exception is an error that happens while a program is running.

Exception handling lets a program respond to errors instead of stopping immediately.

## Basic `try` and `except`
Put code that might fail inside `try`.

Handle the error with `except`.

```python
try:
    number = int("hello")
except ValueError:
    print("That is not a valid number")
```

`int("hello")` raises `ValueError`, so the `except` block runs.

## Handling Specific Exceptions
Catch the exception types you expect.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Specific exceptions make code easier to understand and safer to debug.

## Handling Multiple Exceptions
Use multiple `except` blocks when errors need different handling.

```python
try:
    value = int(input("Number: "))
    result = 10 / value
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Use a tuple when the handling is the same.

```python
try:
    value = int("hello")
except (ValueError, TypeError):
    print("Invalid value")
```

## The `else` Block
The `else` block runs only if no exception occurs.

```python
try:
    value = int("10")
except ValueError:
    print("Invalid number")
else:
    print("Converted:", value)
```

Use `else` for code that should run only after the `try` block succeeds.

## The `finally` Block
The `finally` block always runs.

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File missing")
finally:
    print("Finished")
```

`finally` is often used for cleanup.

For files, a `with` statement is usually better.

## Raising Exceptions
Use `raise` to create an exception yourself.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age
```

Raise an exception when the function cannot safely continue.

## Getting the Error Message
Use `as` to store the exception object.

```python
try:
    value = int("hello")
except ValueError as error:
    print(error)
```

## Common Built-in Exceptions
| Exception | Common Cause |
|-----------|--------------|
| `ValueError` | right type, invalid value |
| `TypeError` | wrong type for an operation |
| `ZeroDivisionError` | division by zero |
| `FileNotFoundError` | file does not exist |
| `KeyError` | dictionary key does not exist |
| `IndexError` | list or tuple index does not exist |
| `ImportError` | import failed |

## Common Mistakes
- Catching every error with a bare `except:`.
- Catching `Exception` when a specific exception would be better.
- Hiding errors without logging or explaining them.
- Putting too much code inside one `try` block.
- Forgetting that `finally` runs even when an error happens.

## Summary
- Exceptions are runtime errors.
- Use `try` and `except` to handle expected errors.
- Catch specific exception types.
- Use `else` for success-only code.
- Use `finally` for cleanup.
- Use `raise` when your code needs to signal an error.
