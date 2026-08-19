# Functions

Source: `Basics/8_functions.py`

## Definition
A function is a callable object that binds parameters to arguments, executes a body, and returns a value. `def` is a **statement** — at runtime it builds a function object from the body and binds it to the given name in the current namespace. Redefining rebinds.

```python
def even_odd(x):
    return "even" if x % 2 == 0 else "odd"

even_odd(10)              # 'even'
```

`def` executes top-to-bottom; a function defined inside a conditional exists only if that branch runs.

## Parameters and arguments
- **Positional** — matched by order.
- **Keyword** — matched by name; order-independent.
- **Default** — evaluated once at `def` time (see Gotchas).

```python
def student(fname, lname="Unknown"):
    print(fname, lname)

student("vamsi")                          # positional
student(fname="vamsi", lname="p")         # keyword
student(lname="p", fname="vamsi")         # order irrelevant
```

## Positional-only `/` and keyword-only `*`
Markers restrict how arguments may be passed.

```python
def f(a, b, /, c, *, d, e):
    ...
# a, b — positional only     (must NOT use a=..., b=...)
# c    — positional or keyword
# d, e — keyword only        (must use d=..., e=...)
```

Use `/` to reserve parameter names for future kwargs; use `*` to force call sites to name arguments for readability.

## `*args` and `**kwargs`
- `*args` — extra positional arguments collected into a **tuple**.
- `**kwargs` — extra keyword arguments collected into a **dict**.

```python
def log(*args, **kwargs):
    print(args, kwargs)

log("hi", "world", user="v", n=3)
# ('hi', 'world') {'user': 'v', 'n': 3}
```

Call-site unpacking is the inverse:
```python
log(*["hi", "world"], **{"user": "v"})
```

## Parameter order
Signature order is fixed:

```
positional  →  *args  →  keyword-only  →  **kwargs
```

```python
def f(a, b=1, *args, key="x", **kwargs): ...
```

Only one `*args` and one `**kwargs` per signature.

## Return values
- No `return`, or bare `return` → returns `None`.
- Multiple values → returned as a tuple; unpack at the call site.

```python
def stats(xs):
    return min(xs), max(xs)             # tuple

lo, hi = stats([3, 1, 2])
```

## How call binding works
Python is **pass-by-object-reference**. The parameter is a new local name bound to the same object the caller passed. Consequences:

- **Rebinding** the parameter (`x = 20`) affects only the local name.
- **Mutating** the object (`x.append(1)`, `x[0] = 9`) is visible to the caller.

```python
def rebind(a):  a = 20                  # local only
def mutate(x):  x[0] = 20               # caller sees it

n = 10;         rebind(n);   n          # 10
lst = [10,20];  mutate(lst); lst        # [20, 20]
```

Immutable objects (`int`, `str`, `tuple`) can't be mutated, so only rebinding is possible.

## Scope
Names in a function body follow the **LEGB** lookup order: Local → Enclosing → Global → Built-in. Full treatment in [11_Scope_and_Namespaces.md](11_Scope_and_Namespaces.md).

## Lambdas
A `lambda` is a **single-expression** function object. No statements, no `return` keyword — the expression is the return value.

```python
square = lambda x: x * x
sorted(words, key=lambda s: len(s))
```

Reach for `def` for anything that needs `if/else` blocks, loops, or multiple statements. Deep coverage in [13_Advanced_Functions.md](13_Advanced_Functions.md).

## First-class objects
Function objects can be assigned, passed, returned, and stored.

```python
def show(): print("hi")

f = show                                # bind another name
f()                                     # 'hi'

ops = {"upper": str.upper, "lower": str.lower}
ops["upper"]("hi")                      # 'HI'
```

## Type hints
Annotations declare intended types; the interpreter does not enforce them. Full treatment in [12_Type_Hints.md](12_Type_Hints.md).

```python
def add(a: int, b: int) -> int:
    return a + b
```

## Gotchas
- **Mutable default trap** — `def f(x, acc=[])` evaluates `[]` **once** at `def` time; the same list is reused across calls. Use `None` as a sentinel:
  ```python
  def f(x, acc=None):
      if acc is None: acc = []
      acc.append(x); return acc
  ```
- **Unpacking order at call sites** — positionals before `*iter`, keywords before `**mapping`. Duplicate keys across `**` unpackings raise `TypeError`.
- **`return` vs `yield`** — a function with any `yield` becomes a generator function; calling it returns a generator, it does **not** execute the body.
- **Reassigning `def` names** — the last `def name` wins; there is no overloading by signature.
- **Default expressions capture bindings, not values later** — `def f(x=n)` freezes `n`'s current object at `def` time.
