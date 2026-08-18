# Advanced Functions

Once you're comfortable with `def`, these are the next things to know: functions that take any number of arguments (`*args`, `**kwargs`), tiny one-line functions (`lambda`), passing functions as values, and functions that remember variables (closures).

## `*args` — variadic positional arguments
Collect any number of extra positional arguments into a **tuple** named `args`.
```python
def total(*args):
    return sum(args)

total(1, 2, 3)              # 6
total()                     # 0
total(*[1, 2, 3])           # 6 — unpacking on the call side
```
The name `args` is convention — `*nums` is equally valid.

## `**kwargs` — variadic keyword arguments
Collect any number of extra keyword arguments into a **dict** named `kwargs`.
```python
def make_user(**kwargs):
    return kwargs

make_user(name="Vamsi", age=25)
# {'name': 'Vamsi', 'age': 25}

data = {"name": "V", "age": 25}
make_user(**data)           # same as above — dict-unpacking on call
```

## Full parameter order
When you combine them, this is the required order:
```python
def f(pos1, pos2, /, pos_or_kw, *, kw_only1, kw_only2):
    ...

def g(a, b=1, *args, key="x", **kwargs):
    ...
```
- `/` — everything before is **positional-only**.
- `*` (or `*args`) — everything after is **keyword-only**.

## The mutable-default trap
Default values are evaluated **once**, at function-definition time — not on each call. Mutable defaults are shared across calls.
```python
def append_bad(x, target=[]):       # BAD
    target.append(x)
    return target

append_bad(1)       # [1]
append_bad(2)       # [1, 2]   ← same list!
append_bad(3)       # [1, 2, 3]
```
Idiom: use `None` as the sentinel and create a fresh object inside.
```python
def append_ok(x, target=None):
    if target is None:
        target = []
    target.append(x)
    return target
```

## Lambdas — anonymous functions
A `lambda` is a **single-expression** function. No statements, no `return` keyword (the expression is returned implicitly).
```python
square = lambda x: x * x
square(5)                   # 25

add = lambda a, b: a + b
```
Prefer `def` for anything non-trivial — lambdas are best when passed inline to another function:
```python
sorted(["banana", "fig", "apple"], key=lambda s: len(s))
# ['fig', 'apple', 'banana']
```

## First-class functions
Functions are objects — you can pass them, return them, and store them in data structures.
```python
def apply(fn, x):
    return fn(x)

apply(str.upper, "hi")      # 'HI'
apply(lambda n: n * 2, 5)   # 10

ops = {"add": lambda a, b: a + b, "mul": lambda a, b: a * b}
ops["add"](2, 3)            # 5
```
Common consumers: `map`, `filter`, `sorted(key=...)`, `min/max(key=...)`, `functools.reduce`.

## Closures
A **closure** is a function that remembers variables from the enclosing scope where it was defined, even after that scope has finished executing.
```python
def make_multiplier(n):
    def mul(x):
        return x * n            # `n` is captured from the enclosing scope
    return mul

double = make_multiplier(2)
triple = make_multiplier(3)
double(5)       # 10
triple(5)       # 15
```
To **rebind** (not just read) a captured name, use `nonlocal` — see [11_Scope_and_Namespaces.md](11_Scope_and_Namespaces.md).
```python
def counter():
    count = 0
    def bump():
        nonlocal count
        count += 1
        return count
    return bump
```

## Return-value conventions
- A function with no `return` implicitly returns `None`.
- Return **multiple values** by returning a tuple; the caller can unpack.
```python
def divmod2(a, b):
    return a // b, a % b

q, r = divmod2(10, 3)       # 3, 1
```

## Gotchas
- **Mutable defaults** are the #1 Python beginner trap — always use `None` + create-inside.
- **Late binding in closures** — closures capture the *name*, not the value at definition time. Classic pitfall:
  ```python
  fns = [lambda: i for i in range(3)]
  [f() for f in fns]              # [2, 2, 2]  — not [0, 1, 2]
  ```
  Fix by binding with a default argument: `lambda i=i: i`.
- **Lambdas are expressions, not statements** — no `if/elif`, no `return`, no assignment. Reach for `def` when you need any of these.
- **`*args` collects into a tuple, `**kwargs` into a dict** — even when only one extra arg is passed.
- **Only one `*args` and one `**kwargs` per signature.** Order is fixed: positional → `*args` → keyword-only → `**kwargs`.
