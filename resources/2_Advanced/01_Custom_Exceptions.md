# Custom Exceptions

Source: `src/2_Advanced/1_CustomException.py`

## Definition
A custom exception is a class that represents an application-specific error. It should usually inherit from `Exception`.

Custom exceptions make error handling clearer because callers can catch a meaningful error type instead of a generic one.

## Basic custom exception
```python
class MyException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
```

`super().__init__(message)` passes the error message to Python's built-in exception machinery so printing the exception works naturally.

```python
err = MyException("My Error Message")
print(err)                     # My Error Message
```

## Custom exception with extra data
Add attributes when the caller needs structured information about the error.
```python
class MyException2(Exception):
    def __init__(self, message: str, errorCode: int):
        super().__init__(message)
        self.message = message
        self.errorCode = errorCode

    def __str__(self):
        return f"{self.message}, (errorCode: {self.errorCode})"
```

`__str__()` controls the string shown by `print(error)`.
```python
err2 = MyException2("Error Message 2", 400)
print(err2)                    # Error Message 2, (errorCode: 400)
```

## Raising a custom exception
Use `raise` when a function cannot complete normally.
```python
def divide(num1: int, num2: int):
    if num2 == 0:
        raise MyException("Divide By Zero Error")
    return num1 / num2
```

When `num2` is `0`, execution stops at the `raise` line and control moves to a matching `except` block.

## Handling a custom exception
```python
try:
    divide(3, 0)
except MyException as e:
    print(e)
```

The `except MyException` block catches only `MyException` and its subclasses.

## Naming convention
Production custom exceptions usually end with `Error`.
```python
class DivideByZeroError(Exception):
    pass
```

The name should describe the failure, not the implementation.

## Why use custom exceptions
- Clearer error meaning: `DivideByZeroError` is more specific than `Exception`.
- Targeted handling: callers can catch only the errors they know how to recover from.
- Extra details: attributes like `errorCode` can carry structured context.

## Common pattern
```python
class AppError(Exception):
    """Base class for application errors."""


class ValidationError(AppError):
    pass


class PaymentError(AppError):
    pass
```

A base custom exception lets callers catch all application errors with `except AppError`.

## Gotchas
- **Inherit from `Exception`**, not `BaseException`.
- **Call `super().__init__(message)`** so the message is stored correctly.
- **Do not catch broad exceptions unnecessarily** — prefer catching the specific custom exception.
- **Use `raise`, not `return`, for errors** that should interrupt normal control flow.
- **Do not hide errors with empty `except` blocks** — log or handle them intentionally.
