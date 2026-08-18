# Truthiness

## What is truthiness?
In Python, any value can act like `True` or `False` in an `if` statement — you don't need to write `== True`. This "does it behave like True?" behavior is called **truthiness**. Empty things (`0`, `""`, `[]`, `None`) are **falsy**; everything else is **truthy**.

## Falsy values
The common built-in falsy values:
```python
False
None
0                # int
0.0              # float
0j               # complex
""               # empty string
b""              # empty bytes
[]               # empty list
()               # empty tuple
{}               # empty dict
set()            # empty set
frozenset()      # empty frozenset
bytearray()      # empty bytearray
range(0)         # empty range
```
**Everything else is truthy** — including `"False"` (a non-empty string), `[0]` (a list with one element), and `-1`.

## Using truthiness
```python
name = ""
if name:                 # cleaner than: if name != ""
    print("has name")
else:
    print("empty")

items = [1, 2, 3]
if items:                # cleaner than: if len(items) > 0
    print(items[0])
```

## `bool()` — the explicit form
```python
bool(0)          # False
bool("")         # False
bool([])         # False
bool("hi")       # True
bool([0])        # True   ← non-empty list, even though its element is falsy
```

## Short-circuit `and` / `or`
These operators do **not** return booleans — they return one of their operands:
- `x and y` — returns `x` if `x` is falsy, else `y`.
- `x or y` — returns `x` if `x` is truthy, else `y`.

```python
0 and 5              # 0    ← short-circuits on falsy left operand
1 and 5              # 5
None or "default"    # 'default'
"hi" or "default"    # 'hi'
```

This is why the idiom `name = user_input or "guest"` works — pick the first truthy value.

## `not`
Unary operator that always returns a real `bool`.
```python
not 0            # True
not [1, 2]       # False
not None         # True
```

## Truthy vs `== True` — a common pitfall
Never use `== True` / `== False` in conditions. It's noisier and, for non-bool values, wrong.
```python
x = 1
if x == True:    # True  (only because 1 == True in Python)
    ...
if x is True:    # False  (x is int, not the bool object)
    ...
if x:            # True  ← the right way
    ...
```

## Gotchas
- **`None` vs falsy** — use `if x is None:` when you specifically mean "is `None`". `if not x:` also matches `0`, `""`, `[]`, etc.
- **Custom objects** — a class can override `__bool__` (or `__len__`) to control truthiness. Missing both, instances are always truthy.
- **`bool` is a subclass of `int`** — `True == 1` and `False == 0` are both `True`. Use `is True` only when you truly need identity.
- **Short-circuit returns operands, not booleans** — `1 or 2` is `1`, not `True`. Wrap in `bool(...)` if you specifically need a boolean.
