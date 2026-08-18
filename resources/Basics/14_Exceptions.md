# Exceptions

## What is an exception?
An **exception** is Python's way of saying "something went wrong" — a missing file, a bad index, a divide by zero. If you don't catch it, the program crashes and prints an error. Handling exceptions lets you catch the problem and keep the program running.

## `try` / `except`
Wrap the risky operation; catch by exception class.
```python
try:
    n = int(input("number: "))
    print(10 / n)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("can't divide by zero")
```
Match the **most specific** class you actually intend to handle — never a bare `except:`.

## `except` with the exception object
```python
try:
    open("missing.txt")
except FileNotFoundError as e:
    print(f"file missing: {e.filename}")
```

## `else` — runs when no exception was raised
Put in the `else` block anything that should run **only if the `try` succeeded**. Keeps the `try` narrow.
```python
try:
    data = fetch()
except NetworkError:
    print("fetch failed")
else:
    process(data)           # runs only if fetch() didn't raise
```

## `finally` — always runs
Cleanup code that must execute whether the `try` succeeded, raised, or returned early.
```python
f = open("file.txt")
try:
    process(f)
finally:
    f.close()               # runs even if process(f) raised
```
For file/lock/DB cleanup, prefer a **context manager** (`with` statement) — see [15_Context_Managers.md](15_Context_Managers.md).

## Raising exceptions
Use `raise` with an exception instance (or class).
```python
def sqrt(x):
    if x < 0:
        raise ValueError(f"cannot sqrt negative: {x}")
    return x ** 0.5
```

## Re-raising
Bare `raise` inside an `except` block re-raises the current exception, preserving the traceback.
```python
try:
    do_thing()
except Exception:
    log("do_thing failed")
    raise                   # re-raise, don't swallow
```

## Exception chaining — `raise ... from ...`
Preserves both the new and the original exception in the traceback — signals "the second was **caused by** the first".
```python
try:
    int(user_input)
except ValueError as e:
    raise RuntimeError("bad config") from e
```
Use `from None` to suppress the original if you specifically want a clean traceback.

## Common built-in exceptions
| Exception | Raised when |
|-----------|-------------|
| `ValueError` | right type, wrong value (e.g. `int("abc")`) |
| `TypeError` | wrong type (e.g. `"a" + 1`) |
| `KeyError` | dict key missing (`d["missing"]`) |
| `IndexError` | sequence index out of range (`a[99]`) |
| `AttributeError` | attribute missing (`obj.foo` and no `foo`) |
| `NameError` | name is not defined |
| `ZeroDivisionError` | divide by zero |
| `FileNotFoundError` | file doesn't exist |
| `StopIteration` | iterator exhausted |
| `RuntimeError` | generic error not fitting the above |

They all inherit from `Exception`, which inherits from `BaseException`. Catch `Exception` (not `BaseException`) as a last resort — `BaseException` also catches `KeyboardInterrupt` / `SystemExit`, which you almost never want to swallow.

## Custom exceptions
Subclass `Exception` (or a more specific class).
```python
class InvalidUserError(Exception):
    """Raised when a user record fails validation."""

class UserNotFoundError(InvalidUserError):
    pass

try:
    load_user(42)
except InvalidUserError as e:      # catches both subclasses
    log(str(e))
```
Give them descriptive names ending in `Error`; add attributes if callers need structured info.

## Multiple exception types in one clause
```python
try:
    parse(x)
except (ValueError, TypeError) as e:        # tuple, not or
    print(f"bad input: {e}")
```

## Gotchas
- **Never use bare `except:` or `except BaseException:`** — they catch `KeyboardInterrupt` and `SystemExit` too. Use `except Exception:` if you truly need a catch-all.
- **Don't silently pass** — `except X: pass` hides real bugs. At minimum, log it.
- **`except` clauses match by isinstance** — a subclass is caught by a base class. Order clauses **most-specific first**, or the specific `except` will be shadowed.
- **`try` scope**: names assigned inside `try` are visible outside, but if the assignment raised before completing, using them raises `UnboundLocalError` / `NameError`.
- **`else` runs only when no exception was raised** — not when one was raised and handled.
- **`finally` runs even on `return`** — including when it itself returns/raises, which overrides the try's return value. Rarely what you want.
