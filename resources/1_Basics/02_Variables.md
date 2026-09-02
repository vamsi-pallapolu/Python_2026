# Variables

Source: `Basics/2_variables.py`

## Definition
A variable in Python is a **name bound to an object**. Names live in a namespace (module, function, class); the object lives on the heap. Assignment binds a name to an object — it does not copy the object, and it does not declare a type. The same name can be rebound to objects of different types over its lifetime.

## Assignment forms
```python
x = 10                          # single binding
a = b = c = 0                   # chained — all names bind to the same object
x, y = 1, 2                     # tuple unpacking
x, y = y, x                     # swap (no temporary)
a, *rest = [1, 2, 3, 4]         # a=1, rest=[2,3,4]
*init, last = [1, 2, 3, 4]      # init=[1,2,3], last=4
```

Chained assignment evaluates the right-hand side **once** and binds every name to that single object. For mutables this means shared state:
```python
a = b = []
a.append(1)
b                               # [1] — same list
```

## Reference semantics
Every value is an object; every variable is a reference. Rebinding changes what a name points to; mutation changes the object itself.
```python
x = 1
y = x
y = y + 1                       # y rebinds to a new int; x unchanged

a = [1, 2]
b = a
b.append(3)
a                               # [1, 2, 3] — aliased mutable
```

Passing a variable to a function passes the reference. Rebinding inside the function is local; mutation is visible to the caller.

## Identity vs equality
- `x is y` — same object (`id(x) == id(y)`).
- `x == y` — equal value (`__eq__`).
```python
v1 = [1, 2, 3]
v2 = [1, 2, 3]
v1 == v2                        # True
v1 is v2                        # False
id(v1), id(v2)                  # distinct
```

`is` is reserved for singletons — `None`, `True`, `False`, sentinel objects. For value comparison, always use `==`.

## `del`
Unbinds the name from the namespace. The object is garbage-collected when its last reference disappears.
```python
z = 30
del z
z                               # NameError
```

`del lst[i]` and `del d[k]` invoke `__delitem__` — a different operation.

## Naming
- Identifiers: `[A-Za-z_][A-Za-z0-9_]*`, case-sensitive.
- Reserved words (`if`, `class`, `def`, ...) cannot be used.
- PEP 8:
  - `snake_case` — variables, functions, modules.
  - `PascalCase` — classes.
  - `UPPER_SNAKE` — module-level constants.
  - `_leading` — internal use hint.
  - `__dunder__` — reserved for the language.

## Walrus operator `:=`
Assigns inside an expression. The bound name is available in the surrounding scope.
```python
if (n := len(data)) > 10:
    print(f"too long: {n}")

while chunk := f.read(4096):
    process(chunk)

# in comprehensions — evaluate once per element
result = [y for x in data if (y := f(x)) is not None]
```

## Semantics
Assignment `name = expr` evaluates `expr` to an object, then binds `name` in the current namespace to that object. Augmented assignment `name op= expr` calls `__iop__` (in-place) if defined, else falls back to `name = name op expr`. On mutables (`list.__iadd__`) it mutates in place; on immutables (`int`, `tuple`) it rebinds.
```python
xs = [1]
ys = xs
xs += [2]                       # list.__iadd__ — mutates
ys                              # [1, 2]

n = 1
m = n
n += 1                          # int has no __iadd__ — rebinds
m                               # 1
```

## Gotchas
- **Chained assignment shares one object** — `a = b = []` gives two names for the same list.
- **Augmented assignment differs on mutable vs immutable** — mutates or rebinds.
- **`is` for value comparison is unreliable** — `a = 1000; b = 1000; a is b` is implementation-defined. Small integers and interned strings may look identical by accident.
- **Loop / comprehension variables leak (or don't)** — plain `for i in ...` leaves `i` bound; comprehensions have their own scope.
- **Mutable default arguments** — `def f(x=[])` shares the same list across calls. Use `None` as the sentinel.
- **Deleting an attribute vs a name** — `del obj.attr` triggers `__delattr__`; `del obj` just unbinds `obj`.
