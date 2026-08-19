# Type Hints

## Definition
Type hints are **annotations** on variables, parameters, and return values. They are not enforced at runtime — the interpreter stores them but does not check them. Their consumers are static type checkers (`mypy`, `pyright`), IDEs, and libraries that introspect annotations at runtime.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Passing `add("1", "2")` runs without error at runtime; only a checker will flag it.

## Variable annotations
```python
name: str = "Vamsi"
age: int = 25
scores: list[int] = [90, 85, 78]

count: int                  # annotation only, no binding
```

An annotation-only statement records the type in `__annotations__` without creating a variable.

## Function annotations
Parameters use `: type`; the return uses `-> type`. `None` means the function returns nothing meaningful.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def log(msg: str) -> None:
    print(msg)
```

## Built-in generics (3.9+)
```python
list[int]
dict[str, int]
tuple[int, str]             # exactly (int, str)
tuple[int, ...]              # any-length tuple of ints
set[str]
```

On 3.8 and earlier, import from `typing` (`List`, `Dict`, `Tuple`, `Set`) instead.

## Unions and Optional
`X | Y` requires 3.10+; older code uses `typing.Union`.

```python
def parse(x: int | str) -> int:
    return int(x)

# Optional[X] is exactly X | None
def find(uid: int) -> str | None:
    ...
```

`Optional[X]` means "value or None". It does **not** mean "the parameter is optional" — that's controlled by giving the parameter a default value.

## typing helpers
| Helper | Meaning |
|--------|---------|
| `Any` | disables checking for this slot |
| `Callable[[Arg1, Arg2], Ret]` | callable with a given signature |
| `Iterable[X]` / `Iterator[X]` | supports `iter()` / `next()` |
| `Sequence[X]` | indexable, has `len` (list, tuple, str) |
| `Mapping[K, V]` | read-only dict-like |

```python
from typing import Callable, Iterable

def apply(fn: Callable[[int], int], xs: Iterable[int]) -> list[int]:
    return [fn(x) for x in xs]
```

## Protocols — structural typing
`Protocol` defines an interface by the presence of methods/attributes; anything with a matching shape satisfies it, no inheritance required.

```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...

def shut(x: SupportsClose) -> None:
    x.close()
```

## Generics with `TypeVar`
```python
from typing import TypeVar
T = TypeVar("T")

def first(xs: list[T]) -> T:
    return xs[0]
```

3.12+ has clean parameterized syntax without importing `TypeVar`:
```python
def first[T](xs: list[T]) -> T:
    return xs[0]
```

## Literal, Final, ClassVar
```python
from typing import Literal, Final, ClassVar

Mode = Literal["r", "w", "a"]
def open_file(path: str, mode: Mode) -> None: ...

PI: Final = 3.14159         # not to be reassigned (checker-enforced)

class C:
    total: ClassVar[int] = 0    # class attribute, not per-instance
```

## TypedDict
Dicts with a fixed key schema, checked structurally.

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

u: User = {"name": "v", "age": 25}
```

## Type aliases
```python
# 3.12+ — real alias syntax
type UserId = int
type UserMap = dict[UserId, str]

# Any version — plain assignment
UserId = int
UserMap = dict[UserId, str]
```

## Forward references and `__future__`
Referencing a name before it's defined requires quoting or deferring evaluation.

```python
def f(node: "TreeNode") -> None: ...        # string forward ref

# Or defer all annotations to strings:
from __future__ import annotations
def f(node: TreeNode) -> None: ...
```

With `from __future__ import annotations`, every annotation is stored as a string; runtime consumers must call `typing.get_type_hints(obj)` to resolve them.

## Runtime access
- `obj.__annotations__` — raw annotation mapping.
- `typing.get_type_hints(obj)` — resolves strings and forward refs.
- `typing.cast(T, value)` — checker-only assertion; no runtime effect.
- `@overload` — declare multiple typed signatures for one implementation.

```python
from typing import overload

@overload
def f(x: int) -> int: ...
@overload
def f(x: str) -> str: ...
def f(x):
    return x
```

## Static checking
```bash
pip install mypy
mypy your_file.py
```

`pyright` (used by Pylance in VS Code) is a faster alternative with slightly different defaults.

## Gotchas
- **Not runtime-enforced.** Passing the wrong type does not raise; only a checker flags it.
- **`list[int]` needs 3.9+; `X | Y` needs 3.10+.** On older versions use `typing.List` / `typing.Union`.
- **`Optional[X]` ≠ "optional parameter".** It means "X or None". A parameter is optional when it has a default value.
- **Forward references need quoting or `__future__`.** Otherwise Python evaluates the annotation at `def` time and raises `NameError`.
- **`from __future__ import annotations` breaks runtime introspection.** Libraries reading `__annotations__` directly will see strings; use `typing.get_type_hints`.
- **`Any` silently disables checking.** Prefer `object` when you truly mean "any object" and want the checker to still restrict operations.
