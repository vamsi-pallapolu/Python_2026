# Exceptions

## Definition
An **exception** is a runtime error signalled by raising an object of the exception hierarchy. Unhandled, it unwinds the stack and terminates the program with a traceback. Handling redirects control to a matching `except` clause.

## `try` / `except`
Wrap the risky code; match by exception class (`isinstance` semantics — subclasses are caught by base classes).
```python
try:
    n = int(input("number: "))
    print(10 / n)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Order clauses **most-specific first**; a base-class clause listed first shadows later specific ones.

## Multiple types in one clause
```python
try:
    parse(x)
except (ValueError, TypeError) as e:      # tuple, not `or`
    log(e)
```

## Binding with `as`
Binds the exception instance to a name **only within the clause body** — the name is deleted on exit to break reference cycles with the traceback.
```python
try:
    open("missing.txt")
except FileNotFoundError as e:
    print(e.filename)
# e is no longer in scope here
```

## `else` — ran when `try` succeeded
Runs only when no exception was raised. Keeps the `try` block narrow — only the operation that can fail sits inside `try`.
```python
try:
    data = fetch()
except NetworkError:
    log("fetch failed")
else:
    process(data)             # runs only when fetch() succeeded
```

## `finally` — always runs
Executes on any exit path: fall-through, exception (handled or not), `return`, `break`, `continue`.
```python
try:
    work()
    return 1
finally:
    cleanup()                 # runs before the return actually returns
```
A `return` or `raise` inside `finally` **overrides** the `try`'s return value or in-flight exception. Rarely intended.

## `raise` and re-raise
```python
raise ValueError(f"bad input: {x!r}")     # new exception

try:
    do_thing()
except Exception:
    log("failed")
    raise                                  # re-raise current — keeps traceback
```

## Exception chaining
`raise X from Y` sets `X.__cause__ = Y` — the traceback prints "The above exception was the direct cause of the following exception". If a new exception is raised implicitly inside an `except` block, Python sets `__context__` and prints "During handling of the above exception...".
```python
try:
    int(user_input)
except ValueError as e:
    raise RuntimeError("bad config") from e     # explicit cause
```
`raise X from None` suppresses the chain — clean traceback with no origin.

## Exception hierarchy
```
BaseException
 ├── SystemExit                (sys.exit)
 ├── KeyboardInterrupt         (Ctrl-C)
 ├── GeneratorExit             (generator .close())
 └── Exception
      ├── ArithmeticError      → ZeroDivisionError, OverflowError, FloatingPointError
      ├── LookupError          → IndexError, KeyError
      ├── OSError              → FileNotFoundError, PermissionError, ...
      ├── ValueError, TypeError, AttributeError, NameError, RuntimeError, StopIteration, ...
```
Catch `Exception`, **never** `BaseException` — the latter swallows `KeyboardInterrupt` and `SystemExit`. Bare `except:` is equivalent to `except BaseException:` — don't use it.

## Custom exceptions
Subclass `Exception` (or a more specific class). Name ends in `Error`. Add attributes if callers need structured info.
```python
class InvalidUserError(Exception):
    """User record failed validation."""

class UserNotFoundError(InvalidUserError):
    pass

try:
    load_user(42)
except InvalidUserError as e:      # catches both
    log(e)
```

## `assert` is not for validation
`assert cond, msg` raises `AssertionError` when `cond` is falsy. All `assert` statements are **stripped when Python runs with `-O`** — use them for internal invariants, never for user-input validation or security checks.
```python
assert isinstance(x, int), "internal invariant"     # ok — debug aid
if x < 0: raise ValueError(...)                     # ok — real check
```

## `ExceptionGroup` and `except*` (3.11+)
Represents multiple exceptions raised concurrently — used by `asyncio.TaskGroup` and any code that must surface several failures. `except*` matches by type and produces a subgroup.
```python
try:
    run_tasks()
except* ValueError as eg:
    for e in eg.exceptions: log(e)
except* (OSError, RuntimeError) as eg:
    handle(eg)
```

## Semantics
- Matching uses `isinstance(exc, clause_type)`.
- First matching clause wins; remaining clauses are skipped.
- The exception object is set on `sys.exc_info()` for the duration of the clause.
- `finally` executes before the exception propagates or the `return` completes.

## Gotchas
- **Bare `except:`** or `except BaseException:` catches `KeyboardInterrupt` and `SystemExit`.
- **Silent `except X: pass`** hides bugs — at minimum, log.
- **Clause ordering** — most-specific first, or a base class shadows subclasses.
- **`finally` return/raise overrides** the `try`'s return or in-flight exception.
- **`as e` is scoped to the clause** — reference outside raises `NameError`.
- **`assert` disappears under `-O`** — never rely on it for validation.
- **Chaining defaults** — inside an `except`, a fresh `raise NewError(...)` still records `__context__`; use `from None` to hide it when it's noise.
