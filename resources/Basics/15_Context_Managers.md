# Context Managers (`with` statement)

## What is a context manager?
A context manager is a helper you use with the `with` keyword to guarantee cleanup. The most common case: opening a file with `with open(...) as f:` — Python automatically closes the file when the block ends, even if something goes wrong inside.

## Basic usage
```python
with open("file.txt") as f:
    data = f.read()
# f.close() is called automatically here — even if read() raised
```
Compare to the manual equivalent:
```python
f = open("file.txt")
try:
    data = f.read()
finally:
    f.close()
```
Same behavior — `with` is shorter, safer, and idiomatic.

## The protocol — `__enter__` / `__exit__`
A context manager is any object with two methods:
- `__enter__(self)` — runs at the start of the block; its return value is bound to the name after `as`.
- `__exit__(self, exc_type, exc_val, exc_tb)` — runs when the block exits, whether normally or via exception. Return `True` to *suppress* an exception (rare).

```python
class Timer:
    def __enter__(self):
        self.start = time_now()
        return self                     # what `as t` binds to

    def __exit__(self, exc_type, exc, tb):
        print(f"elapsed: {time_now() - self.start}")
        # return None (falsy) → don't suppress exceptions

with Timer() as t:
    do_work()
```

## Multiple context managers
Nest them by chaining with commas — each unwinds in reverse order on exit.
```python
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())
```
Equivalent to nested `with` blocks.

## `contextlib.contextmanager` — turn a generator into a context manager
The decorator lets you write a context manager as a **single function** with a `yield`.
```python
from contextlib import contextmanager

@contextmanager
def timer():
    start = time_now()
    try:
        yield                       # everything before `yield` = __enter__
    finally:
        print(f"elapsed: {time_now() - start}")   # after `yield` = __exit__

with timer():
    do_work()
```
The `try / finally` ensures teardown runs even if the caller's block raises.

## Common built-in context managers
| Context manager | Use |
|-----------------|-----|
| `open(...)` | file handles — closes on exit |
| `threading.Lock()` | acquire on enter, release on exit |
| `contextlib.suppress(Exc)` | swallow specified exceptions inside the block |
| `contextlib.redirect_stdout(f)` | route `print` into a file/buffer |
| `tempfile.TemporaryDirectory()` | temp dir that is deleted on exit |
| DB connections / cursors | commit or rollback the transaction |

## Suppressing exceptions with `contextlib.suppress`
Cleaner than `try / except: pass`.
```python
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("maybe_exists.txt")
```

## Gotchas
- **`__exit__` runs even on exception** — the block's cleanup is guaranteed, but the exception still propagates unless `__exit__` returns `True`. Returning `True` to swallow errors is rarely correct.
- **`with` does not create a new scope** — names bound inside the block (including via `as`) remain visible after the block. Just like `for` and `if`.
- **`as name` binds `__enter__`'s return value, not the context manager itself.** For `open()`, `__enter__` returns the file — so `f` **is** the file object.
- **Exceptions inside `__enter__`** — if `__enter__` raises, `__exit__` is **not** called. Do setup that can fail before opening the context.
- **Reusing the same context manager instance** — most stdlib CMs (like file objects) are single-use; entering twice fails. Create a new one per `with` block.
