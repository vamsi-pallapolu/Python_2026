# Truthiness

## Definition
Truthiness is Python's implicit coercion of any value to `bool` in a boolean context — the condition of `if`/`while`, the operands of `and`/`or`/`not`, the predicates of `any`/`all`/`filter`, and comprehension `if` clauses. The coercion follows a fixed protocol; every object is either truthy or falsy, and user-defined classes can control the outcome.

## Falsy values
The built-in falsy set is closed and small. Everything else is truthy.

```python
False
None
0                # int
0.0              # float
0j               # complex
Decimal(0)       # numeric zero via __bool__
Fraction(0, 1)
""               # empty str
b""              # empty bytes
bytearray()      # empty bytearray
[]               # empty list
()               # empty tuple
{}               # empty dict
set()            # empty set
frozenset()      # empty frozenset
range(0)         # empty range
```

Truthy examples that trip newcomers: `"False"` (non-empty string), `"0"` (non-empty string), `[0]` (one element, even a falsy one), `-1`, `float("nan")`, any live file/socket object.

## `bool()` protocol
`bool(x)` follows a fixed order:

1. Call `type(x).__bool__(x)` if defined; the return must be `True` or `False`.
2. Otherwise call `type(x).__len__(x)`; result `0` is falsy, anything else truthy.
3. Otherwise the object is truthy.

```python
class Bag:
    def __init__(self, items): self.items = items
    def __len__(self):        return len(self.items)   # empty Bag() is falsy

class Always:
    def __bool__(self):       return False             # falsy regardless of state
```

## Short-circuit `and` / `or`
`and` and `or` do not return `True`/`False` — they return the **operand that decided the result** and stop evaluating the rest.

- `x and y` → `x` if `x` is falsy, else `y`.
- `x or y`  → `x` if `x` is truthy, else `y`.

```python
0 and 5              # 0    — left is falsy, short-circuits
1 and 5              # 5    — left truthy, returns right
None or "default"    # 'default'
"hi" or "default"    # 'hi'

name = user_input or "guest"     # first-truthy idiom
```

Chain uses this to pick a first non-empty: `a or b or c or default`.

## `not`
Unary `not` is different — it always returns a real `bool`.

```python
not 0            # True
not [1, 2]       # False
not None         # True
```

## `any` / `all`
Both short-circuit and both handle empty iterables by convention:

```python
any([])          # False   — no truthy element found
all([])          # True    — vacuously true, no counterexample

any(x > 10 for x in nums)    # stops at first truthy
all(x > 0  for x in nums)    # stops at first falsy
```

## `bool` is a subclass of `int`
`True` and `False` are singletons of type `bool`, and `bool` inherits from `int` with `int(True) == 1`, `int(False) == 0`. Useful side effect:

```python
True + True                        # 2
sum(x > 0 for x in nums)           # counts truthy elements
["no", "yes"][bool(flag)]          # index by boolean
```

## `== True` is wrong
Never test truthiness with `== True` / `== False`. It fails for non-bool truthy values.

```python
x = 3
if x == True:    # False — 3 != 1
    ...
if x:            # True  — correct
    ...
```

Use `is None` / `is not None` for the None check specifically; use plain `if x:` for "non-empty / non-zero".

## Gotchas
- **`None` vs empty** — `if not x:` matches `None`, `0`, `""`, `[]`, `{}`. When you specifically mean "is `None`", write `if x is None:`.
- **Custom `__bool__` can lie** — a class that returns `False` from `__bool__` looks empty in conditions even when it holds data (e.g. NumPy arrays raise on ambiguous truthiness instead).
- **Short-circuit returns operands, not booleans** — `1 or 2` is `1`, not `True`. Wrap in `bool(...)` when you need a real boolean (e.g. for JSON serialization).
- **`bool` in arithmetic** — `True == 1` is `True`, but this can mask type bugs. Prefer explicit `int(flag)` when the intent is numeric.
- **NumPy / pandas** — `bool(array)` and `array and other` raise `ValueError` for multi-element arrays. Use `.any()` / `.all()` explicitly.
