# Advanced Functions

## Definition
Beyond `def name(args): ...`, Python treats functions as first-class objects and provides variadic parameters, closures, decorators, and standard-library helpers to compose them. This note covers the patterns needed for real code.

## `*args` and `**kwargs`
Variadic parameters collect the "rest" of the arguments.

- `*args` — extra positional args → **tuple**.
- `**kwargs` — extra keyword args → **dict**.

```python
def log(*args, **kwargs):
    print(args, kwargs)

log("hi", "world", user="v", n=3)
# ('hi', 'world') {'user': 'v', 'n': 3}
```

## Call-site unpacking
The same `*` / `**` syntax at the call site expands an iterable / mapping into arguments.

```python
def f(a, b, c): ...

f(*[1, 2, 3])                   # positional unpack
f(**{"a": 1, "b": 2, "c": 3})   # keyword unpack

# Forwarding wrapper — a common pattern:
def wrap(*args, **kwargs):
    return inner(*args, **kwargs)
```

Positionals must precede `*iter` unpacks, keywords must precede `**mapping` unpacks. Duplicate keys across `**` unpackings raise `TypeError`.

## Parameter order
Full signature order:

```
positional-only  /  positional-or-keyword  *args  keyword-only  **kwargs
```

```python
def f(pos1, pos2, /, pos_or_kw, *args, kw_only, **kwargs):
    ...
```

Only one `*args`, one `**kwargs`. A bare `*` (no name) after positional params introduces keyword-only params without a variadic collector.

## Mutable default trap
Default values are evaluated **once**, at `def` time — not per call. A mutable default is shared across every call.

```python
def append_bad(x, acc=[]):        # BAD
    acc.append(x)
    return acc

append_bad(1)       # [1]
append_bad(2)       # [1, 2]  ← same list
```

Idiom: use `None` as a sentinel, build a fresh object inside.

```python
def append_ok(x, acc=None):
    if acc is None:
        acc = []
    acc.append(x)
    return acc
```

## Lambdas
A `lambda` is a **single expression** that evaluates to a function object. No statements — no `if/elif` blocks, no assignments, no `return` keyword (the expression is the return value). Use `def` otherwise.

```python
square = lambda x: x * x
sorted(words, key=lambda s: len(s))
```

Lambdas are best when passed inline to a higher-order function; naming a lambda (`f = lambda x: ...`) is worse than `def f(x): ...` (worse tracebacks, no docstring).

## First-class functions
Functions are objects. They can be assigned, passed, returned, and stored.

```python
def apply(fn, x): return fn(x)

apply(str.upper, "hi")            # 'HI'
ops = {"add": lambda a,b: a+b, "mul": lambda a,b: a*b}
ops["add"](2, 3)                  # 5
```

## Closures
A closure is a nested function that captures names from its enclosing function's scope. The captured names are looked up in the enclosing scope every time the inner function runs — not frozen at definition.

```python
def make_multiplier(n):
    def mul(x):
        return x * n              # captures n
    return mul

double = make_multiplier(2)
double(5)                          # 10
```

Reading a captured name works implicitly. **Rebinding** it requires `nonlocal`:

```python
def counter():
    n = 0
    def bump():
        nonlocal n
        n += 1
        return n
    return bump
```

See [11_Scope_and_Namespaces.md](11_Scope_and_Namespaces.md) for scope rules.

## Late-binding trap
Closures look up captured names at **call** time, not at `def` time. Loops that create closures over the loop variable all see its final value:

```python
fns = [lambda: i for i in range(3)]
[f() for f in fns]                # [2, 2, 2]  — not [0, 1, 2]
```

Fix by binding the current value as a default argument (defaults are evaluated at `def` time):

```python
fns = [lambda i=i: i for i in range(3)]
[f() for f in fns]                # [0, 1, 2]
```

## Decorators
A decorator is a callable that takes a function and returns a replacement. `@dec` above a `def` is syntactic sugar for `f = dec(f)`.

```python
def trace(fn):
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper

@trace
def add(a, b): return a + b
# equivalent to: add = trace(add)
```

Decorators with arguments desugar to `f = dec(arg)(f)` — the outer call returns the actual decorator.

```python
def repeat(n):
    def deco(fn):
        def wrapper(*a, **kw):
            for _ in range(n): fn(*a, **kw)
        return wrapper
    return deco

@repeat(3)
def hi(): print("hi")
# equivalent to: hi = repeat(3)(hi)
```

Stacked decorators apply **bottom-up**:

```python
@a
@b
def f(): ...
# equivalent to: f = a(b(f))
```

Use `functools.wraps` in the wrapper to copy the wrapped function's `__name__`, `__doc__`, and `__wrapped__`:

```python
from functools import wraps

def trace(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        return fn(*a, **kw)
    return wrapper
```

## `functools` helpers
- `functools.partial(fn, *a, **kw)` — pre-bind arguments.
  ```python
  from functools import partial
  add5 = partial(lambda a, b: a + b, 5)
  add5(10)                          # 15
  ```
- `functools.lru_cache(maxsize=128)` — memoize by argument tuple; args must be hashable.
- `functools.cache` (3.9+) — unbounded memoization.
  ```python
  from functools import cache
  @cache
  def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
  ```

## `operator` helpers
Named-attribute / indexed accessors, often used as `key=` functions.

```python
from operator import itemgetter, attrgetter

sorted(rows, key=itemgetter(1))          # by second column
sorted(users, key=attrgetter("age"))     # by user.age
```

Faster and clearer than `lambda x: x[1]`.

## Callable protocol
Any object with a `__call__` method is callable — functions have no special status. Instances can be callables too:

```python
class Adder:
    def __init__(self, n): self.n = n
    def __call__(self, x): return x + self.n

add5 = Adder(5)
add5(10)                                 # 15
callable(add5)                           # True
```

## Gotchas
- **Mutable defaults** — evaluated once; use `None` sentinel.
- **Late binding in closures** — captured names resolve at call time; fix with `def inner(i=i)` or `partial`.
- **Only one `*args`, one `**kwargs`.** Fixed order: positional → `*args` → keyword-only → `**kwargs`.
- **Decorator without `@wraps`** — loses `__name__`, `__doc__`, and breaks introspection tools (Sphinx, `inspect.signature` fallbacks).
- **`@dec(arg)` vs `@dec`** — the former invokes `dec` first and decorates with its return value. Forgetting the `()` decorates with `dec` itself.
- **`lru_cache` on methods leaks memory** — the cache holds `self`, preventing garbage collection. Use `functools.cached_property` or a WeakValueDictionary instead.
