# Context Managers

## Definition
A context manager runs setup code before a block and cleanup code after the block.

The most common example is opening a file.

```python
with open("notes.txt") as file:
    text = file.read()
```

When the `with` block ends, Python closes the file automatically.

This happens even if an error occurs inside the block.

## Why Use `with`?
Without `with`, you must remember to close the file yourself.

```python
file = open("notes.txt")
try:
    text = file.read()
finally:
    file.close()
```

The `with` version is shorter and safer.

```python
with open("notes.txt") as file:
    text = file.read()
```

## Basic Syntax
```python
with something() as name:
    # use name here
    pass
```

Python does this:

1. Enter the context.
2. Run the block.
3. Exit the context and clean up.

## Common Examples
Files:

```python
with open("data.txt") as file:
    print(file.read())
```

Temporary folders:

```python
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    print(folder)
```

Locks:

```python
from threading import Lock

lock = Lock()

with lock:
    print("Only one thread should do this at a time")
```

## Multiple Context Managers
You can use more than one context manager in the same `with`.

```python
with open("input.txt") as source, open("output.txt", "w") as target:
    target.write(source.read())
```

This opens both files and closes both files when the block ends.

## Custom Context Managers
A context manager usually has two methods:

- `__enter__`: runs before the block
- `__exit__`: runs after the block

```python
class SimpleTimer:
    def __enter__(self):
        from time import time

        self.start = time()
        return self

    def __exit__(self, exc_type, exc, traceback):
        from time import time

        self.elapsed = time() - self.start

with SimpleTimer() as timer:
    total = sum(range(1_000_000))

print(timer.elapsed)
```

The value returned by `__enter__` becomes the value after `as`.

## Creating Context Managers with `contextlib`
For simple context managers, you can write a generator function.

```python
from contextlib import contextmanager
from time import time

@contextmanager
def timer():
    start = time()
    try:
        yield
    finally:
        print(time() - start)

with timer():
    total = sum(range(1_000_000))
```

Code before `yield` runs before the block.

Code after `yield` runs after the block.

## Exception Handling
`__exit__` receives information about errors from the block.

```python
class ShowErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        if exc_type is not None:
            print("Error:", exc)
```

If `__exit__` returns `True`, the error is hidden.

Usually, do not hide errors unless you have a clear reason.

## Useful `contextlib` Tools
Ignore a specific error:

```python
from contextlib import suppress
from pathlib import Path

with suppress(FileNotFoundError):
    Path("missing.txt").unlink()
```

Use a "do nothing" context manager:

```python
from contextlib import nullcontext

with nullcontext():
    print("normal code")
```

Manage many context managers:

```python
from contextlib import ExitStack

paths = ["a.txt", "b.txt"]

with ExitStack() as stack:
    files = [stack.enter_context(open(path)) for path in paths]
    data = [file.read() for file in files]
```

## Common Mistakes
- Forgetting that `with` does not create a new variable scope.
- Returning `True` from `__exit__` by accident and hiding an error.
- Reusing a context manager object that was meant to be used only once.
- Forgetting that `as name` gets the return value of `__enter__`.

## Summary
- Use `with` for resources that need cleanup.
- Files are the most common example.
- Cleanup happens even when an error occurs.
- Custom context managers use `__enter__` and `__exit__`.
- For simple cases, `contextlib.contextmanager` is easier than writing a class.
