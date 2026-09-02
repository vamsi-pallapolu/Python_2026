# Exceptions

Source: `src/1_Basics/9_0_eh.py`

## Definition
An exception is a runtime error condition. Python raises an exception when it cannot continue normal execution.

Exception handling lets the program respond to errors instead of crashing immediately.

## `try`, `except`, `else`, `finally`
```python
try:
    n = 0
    res = 10 / 3
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("The result is:", res)
finally:
    print("Execution completed")
```

| Block | When it runs |
|-------|--------------|
| `try` | code that might raise an exception |
| `except` | when a matching exception happens |
| `else` | when no exception happens |
| `finally` | always runs |

## Specific exception handling
Catch the exact error types you expect.
```python
try:
    x = int("str")
    res = n / x
except ValueError:
    print("Invalid value provided")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("The result is:", res)
finally:
    print("Execution completed")
```

`int("str")` raises `ValueError`, so the `ValueError` block runs.

## Handling multiple exceptions together
Use a tuple of exception classes when the handling is the same.
```python
a = ["10", "twenty", 30]

try:
    res = int(a[0]) + int(a[1])
except (ValueError, TypeError) as e:
    print("Error occurred:", e)
else:
    print("The result is:", res)
finally:
    print("Execution completed")
```

`as e` stores the exception object so its message can be printed.

## Catching general exceptions
```python
try:
    res = 10 / 0
except Exception as e:
    print("An error occurred:", e)
```

This catches most normal application errors. Prefer specific exceptions when possible.

## Raising an exception
Use `raise` to signal an error yourself.
```python
def age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(age)


try:
    age(-5)
except ValueError as e:
    print("Error occurred:", e)
```

Raising an exception is better than returning an invalid result.

## Common built-in exceptions
| Exception | Common cause |
|-----------|--------------|
| `ValueError` | valid type, invalid value |
| `TypeError` | operation used with wrong type |
| `ZeroDivisionError` | division by zero |
| `FileNotFoundError` | missing file |
| `KeyError` | missing dictionary key |
| `IndexError` | invalid sequence index |

## Gotchas
- **Catch specific exceptions first**.
- **`else` runs only if `try` succeeds**.
- **`finally` runs even if an exception was raised**.
- **Do not hide errors with empty `except` blocks**.
- **Use `raise ValueError(...)` for invalid values**.
- **Avoid bare `except:`** because it catches too much.
