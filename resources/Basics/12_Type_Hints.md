# Type Hints

## What are type hints?
Type hints are labels you add to variables and functions to say what type is expected — e.g. "this is an `int`", "this function returns a `str`". Python **does not enforce them at runtime**; they're for you, your IDE, and static checkers like `mypy` to catch mistakes early.

## Variable annotations
```python
name: str = "Vamsi"
age: int = 25
scores: list[int] = [90, 85, 78]
```
The annotation is optional metadata — the value on the right still drives the runtime type.

## Function annotations
Parameters are annotated with `: type`; the return type follows `->`.
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def log(msg: str) -> None:      # None → the function returns nothing meaningful
    print(msg)
```

## Common built-in types
| Hint | Meaning |
|------|---------|
| `int`, `float`, `str`, `bool`, `bytes` | scalars |
| `list[int]` | list of ints |
| `tuple[int, str]` | 2-tuple: int then str |
| `tuple[int, ...]` | tuple of any length, all ints |
| `dict[str, int]` | dict from str keys to int values |
| `set[str]` | set of strings |
| `None` | function returns nothing |

Before Python 3.9, you had to write `List[int]`, `Dict[str, int]`, etc. from the `typing` module. On 3.9+, prefer the lowercase built-in versions.

## Union types — one of several
```python
# Python 3.10+
def parse(x: int | str) -> int:
    return int(x)

# Pre-3.10
from typing import Union
def parse(x: Union[int, str]) -> int: ...
```

## Optional — value or None
`Optional[X]` is exactly `X | None`.
```python
def find_user(uid: int) -> str | None:      # 3.10+
    ...

from typing import Optional                 # older
def find_user(uid: int) -> Optional[str]:
    ...
```

## Any and typing helpers
```python
from typing import Any, Callable, Iterable

def handle(x: Any) -> None: ...                     # opt out of checking
def apply(fn: Callable[[int], int], xs: Iterable[int]) -> list[int]:
    return [fn(x) for x in xs]
```

| Helper | Meaning |
|--------|---------|
| `Any` | any type; disables checking for this slot |
| `Callable[[Arg1, Arg2], Ret]` | a callable with the given signature |
| `Iterable[X]` | anything you can `for x in ...` over |
| `Iterator[X]` | anything you can call `next()` on |
| `Sequence[X]` | list/tuple/str-like (indexable, has `len`) |
| `Mapping[K, V]` | read-only dict-like |

## Type aliases
Give a complex type a readable name.
```python
# 3.12+ syntax
type UserId = int
type UserMap = dict[UserId, str]

# Any version — plain assignment
UserId = int
UserMap = dict[UserId, str]
```

## Static checking
The interpreter ignores hints. To actually catch mismatches, run a checker:
```bash
pip install mypy
mypy your_file.py
```

## Gotchas
- **Hints are not enforced at runtime** — passing a `str` to a parameter hinted `int` will not raise. A type-checker will.
- **`list[int]` requires Python 3.9+** — on older versions, use `from typing import List` and `List[int]`.
- **`X | Y` requires Python 3.10+** — use `Union[X, Y]` on older versions.
- **`Optional[X]` means "X or None"** — not "optional argument". A parameter is made optional by giving it a default value; the type just says "None is also allowed".
- **Forward references** — to reference a class before it's defined, quote the name: `def f(node: "TreeNode"): ...`, or add `from __future__ import annotations` at the top of the file.
