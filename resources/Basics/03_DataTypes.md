# Data Types

Source: `Basics/5_datatypes.py`

## Definition
A type defines the set of values an object can hold and the operations valid on it. Python is **dynamically typed** (types are checked at runtime) and **strongly typed** (no implicit coercion between unrelated types — e.g., `"1" + 1` raises `TypeError`). Every value is an object; `type(x)` returns its class.

## Built-in categories
| Category | Types                              | Mutable? |
|----------|------------------------------------|----------|
| Numeric  | `int`, `float`, `complex`, `bool`  | no       |
| Sequence | `str`, `tuple`, `range`            | no       |
|          | `list`                             | yes      |
| Set      | `frozenset`                        | no       |
|          | `set`                              | yes      |
| Mapping  | `dict`                             | yes      |
| Binary   | `bytes`                            | no       |
|          | `bytearray`, `memoryview`          | yes      |
| None     | `NoneType`                         | —        |

Mutability determines whether an object supports in-place modification and, transitively, whether it is hashable.

## Numeric types
```python
1_000_000               # int — arbitrary precision, no overflow
2 ** 100                # 1267650600228229401496703205376
3.14                    # float — IEEE-754 double (64-bit)
2 + 3j                  # complex
True, False             # bool — subclass of int (True == 1, False == 0)
```

`float` cannot represent most decimals exactly. Compare with tolerance:
```python
0.1 + 0.2 == 0.3                    # False
import math
math.isclose(0.1 + 0.2, 0.3)        # True
```

Special float values:
```python
float("inf"), float("-inf"), float("nan")
math.isnan(x)           # nan != nan, so compare with isnan
```

## Sequences
Ordered, indexable, sliceable. `list` is mutable; `str`, `tuple`, `range` are not.
```python
[1, 2, 3][0]            # 1
(1, 2, 3)[-1]           # 3
"abc"[1:]               # 'bc'
range(10)[::2]          # range(0, 10, 2)
```

## Set and dict
```python
{1, 2, 2, 3}            # {1, 2, 3} — unordered, unique
{"a": 1, "b": 2}["a"]   # 1
```

`set` and `dict` require **hashable** keys/elements. `dict` preserves insertion order (guaranteed since 3.7).

## `None`
Singleton sentinel for "no value". Compare with `is`, not `==`.
```python
x = None
if x is None: ...
```

## Hashability
An object is hashable if it has a stable `__hash__` and `__eq__`. Rule of thumb: **immutable built-ins are hashable; mutable built-ins are not**. A `tuple` is hashable iff all its elements are.
```python
hash((1, 2, "a"))           # ok
hash((1, [2]))              # TypeError — list inside is unhashable
{[1, 2]}                    # TypeError
{(1, 2)}                    # ok
```

## Type conversion
Constructors act as converters. They raise `ValueError` (or `TypeError`) on malformed input.
```python
int("10")               # 10
int("10", 2)            # 2 — base parameter
int(3.9)                # 3 — truncates toward zero
float("3.14")           # 3.14
str(42)                 # '42'
list("abc")             # ['a', 'b', 'c']
tuple([1, 2])           # (1, 2)
set("aab")              # {'a', 'b'}
bool(0), bool(""), bool([])   # all False
```

Safe conversion pattern:
```python
try:
    n = int(s)
except ValueError:
    n = None
```

## `type()` vs `isinstance()`
- `type(x) is T` — exact type match, no subclasses.
- `isinstance(x, T)` — subclass-aware; also accepts a tuple of types.
```python
isinstance(True, int)       # True — bool subclasses int
type(True) is int           # False
isinstance(x, (int, float)) # numeric check
```

Prefer `isinstance` for type checks; use `type()` only when subclass identity matters.

## Gotchas
- **`0.1 + 0.2 != 0.3`** — binary floats can't represent decimal tenths. Use `math.isclose` or `decimal.Decimal`.
- **`True == 1` and `False == 0`** — `bool` is an `int` subclass. `[0, False]` deduplicates via `set` to `{0}`; keys `0` and `False` collide in a `dict`.
- **`tuple` containing a `list` is not hashable** — hashability is deep.
- **`int("3.0")` raises `ValueError`** — use `int(float("3.0"))`.
- **`list("abc")` splits into characters** — pass `[s]` to wrap a single string.
- **`nan == nan` is `False`** — sort/dedup of collections containing `nan` misbehaves. Use `math.isnan`.
- **Chained numeric conversion loses precision** — `int(float("999999999999999999"))` != the original.
