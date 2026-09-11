# Type Hints

## Definition
Type hints tell readers and tools what kind of value you expect.

They do **not** force Python to check types while the program runs.

```python
def add(a: int, b: int) -> int:
    return a + b
```

This says:

- `a` should be an `int`
- `b` should be an `int`
- the function should return an `int`

Python will still run this:

```python
add("1", "2")
```

A type checker can warn you, but Python itself will not stop it.

## Variable Annotations
```python
name: str = "Vamsi"
age: int = 25
price: float = 19.99
is_active: bool = True
```

You can also hint containers.

```python
scores: list[int] = [90, 85, 78]
user: dict[str, str] = {"name": "Vamsi", "city": "New York"}
```

`list[int]` means a list of integers.

`dict[str, str]` means a dictionary with string keys and string values.

## Function Annotations
Use `: type` for parameters.

Use `-> type` for the return value.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def print_total(total: int) -> None:
    print(total)
```

Use `None` when the function does not return a useful value.

## Built-in Collection Types
```python
names: list[str] = ["Asha", "Ben"]
person: dict[str, int] = {"age": 30}
point: tuple[int, int] = (10, 20)
tags: set[str] = {"python", "basics"}
```

For a tuple with many values of the same type:

```python
numbers: tuple[int, ...] = (1, 2, 3, 4)
```

## Union Types
Use `|` when a value can have more than one type.

```python
def parse_id(value: int | str) -> int:
    return int(value)
```

This means `value` can be an `int` or a `str`.

## Optional Values
Use `None` in the type when a value may be missing.

```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Vamsi"
    return None
```

Important: `str | None` means the value can be a string or `None`.

It does not mean the argument is optional.

This parameter is optional because it has a default value:

```python
def greet(name: str = "friend") -> str:
    return f"Hello, {name}"
```

## Type Aliases
A type alias gives a type a clearer name.

```python
UserId = int

def get_user_name(user_id: UserId) -> str:
    return "Vamsi"
```

This can make code easier to read.

## The `Any` Type
`Any` means "allow anything".

```python
from typing import Any

def show(value: Any) -> None:
    print(value)
```

Use `Any` only when you really do not know the type. It disables many useful type checker warnings.

## Callable Types
Use `Callable` for a function that gets passed into another function.

```python
from collections.abc import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def double(x: int) -> int:
    return x * 2

print(apply_twice(double, 3))
```

Output:

```text
12
```

`Callable[[int], int]` means a function that takes one `int` and returns one `int`.

## Static Type Checking
Python does not check type hints by default. Use a tool such as `mypy` or `pyright`.

```bash
pip install mypy
mypy your_file.py
```

Editors like VS Code can also show type hint warnings while you code.

## Common Mistakes
- Thinking type hints change runtime behavior.
- Using `Any` everywhere.
- Forgetting `None` when a function can return nothing.
- Confusing `str | None` with an optional parameter.
- Writing very complex types before the simple types are clear.

## Summary
- Type hints explain expected types.
- They help people, editors, and type checkers.
- They do not make Python enforce types at runtime.
- Use `list[int]`, `dict[str, int]`, and `str | None` for common cases.
- Start simple. Add more detailed hints only when they make the code clearer.
