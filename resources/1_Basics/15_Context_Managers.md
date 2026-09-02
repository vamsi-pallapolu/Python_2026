# Context Managers (`with` statement)

## Definition
A **context manager** guarantees deterministic setup and teardown around a block. `with cm as x:` binds `x` to `cm.__enter__()`, runs the block, then always calls `cm.__exit__(exc_type, exc, tb)` — on normal completion, exception, `return`, `break`, or `continue`.

## Basic usage
```python
with open("file.txt") as f:
    data = f.read()
# f.close() ran here — even if read() raised
```
Manual equivalent:
```python
f = open("file.txt")
try:
    data = f.read()
finally:
    f.close()
```

## The protocol
- `__enter__(self)` — runs at block entry; return value is bound by `as`.
- `__exit__(self, exc_type, exc, tb)` — runs at block exit. Arguments are all `None` on normal exit. **Returning a truthy value suppresses the exception**; falsy/None lets it propagate.

```python
class Timer:
    def __enter__(self):
        self.start = time()
        return self                 # bound by `as t`

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time() - self.start
        # returning None → exception (if any) propagates

with Timer() as t:
    do_work()
print(t.elapsed)
```

## Multiple context managers
Comma-separated form; entered left-to-right, exited **right-to-left** (reverse of entry, like nesting).
```python
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())
```
Equivalent to nested `with` blocks. If the second `__enter__` raises, the first is exited normally.

## `@contextmanager` — generator form
Write a context manager as a generator with a **single `yield`** inside `try/finally`. Code before `yield` is `__enter__`; the yielded value is what `as` binds; code after `yield` is `__exit__`.
```python
from contextlib import contextmanager

@contextmanager
def timer():
    start = time()
    try:
        yield start                 # bound by `as`
    finally:
        print(f"elapsed: {time() - start}")

with timer() as t0:
    do_work()
```
An exception inside the block is re-raised at the `yield`; catch it there to suppress (equivalent to `__exit__` returning `True`).

## `contextlib` toolkit
| Helper | Use |
|---|---|
| `suppress(*Excs)` | swallow listed exceptions inside the block |
| `redirect_stdout(f)` / `redirect_stderr(f)` | route `print` to `f` |
| `nullcontext(x)` | no-op CM — useful when a CM is conditional |
| `closing(obj)` | wrap an object with `.close()` but no CM protocol |
| `ExitStack` | dynamically enter a variable number of CMs |

```python
from contextlib import suppress, ExitStack, nullcontext

with suppress(FileNotFoundError):
    os.remove("maybe.txt")

with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in paths]   # N files, all closed on exit
```

## Async context managers
Implement `__aenter__` and `__aexit__` (coroutines); enter with `async with`. Used for async DB clients, HTTP sessions, locks.
```python
async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
        data = await resp.text()
```

## Common uses
- Files (`open`), locks (`threading.Lock`, `asyncio.Lock`).
- DB transactions — commit on success, rollback on exception.
- Temp resources (`tempfile.TemporaryDirectory`, `tempfile.NamedTemporaryFile`).
- Test doubles (`unittest.mock.patch(...) as mock`).
- Decimal / numpy contexts (`decimal.localcontext`, `np.errstate`).
- Signal masking, working-directory scoping.

## Semantics
- `__exit__` receives `(None, None, None)` on normal exit, else `(type, value, traceback)`.
- Returning `True` from `__exit__` **suppresses** the exception; the `with` statement completes normally.
- If `__enter__` raises, `__exit__` is **not** called — the manager was never entered.
- `with` does not create a new scope; names bound in the block (including `as`) remain visible after.

## Gotchas
- **`__enter__` raising bypasses `__exit__`** — do failable setup before entering the context, or handle cleanup inside `__enter__` itself.
- **Most stdlib CMs are single-use** — a closed file re-entered via `with` fails. Create a new instance per `with`.
- **`as` binds `__enter__`'s return, not the manager** — for `open()`, that happens to be the file object, so `f` is the file. A custom CM that `return self` from `__enter__` behaves the same; one that returns something else does not.
- **Suppressing exceptions** by returning `True` from `__exit__` is rarely correct — usually a bug.
- **`with` doesn't scope names** — variables bound inside remain after the block, including via `as`.
- **`@contextmanager` requires exactly one `yield`** — two `yield`s or an unhandled exception past `yield` breaks the protocol.
