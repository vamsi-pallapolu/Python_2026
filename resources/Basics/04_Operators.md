# Operators

Source: `Basics/3_operators.py`

## Definition
An operator is a syntactic token that invokes a method on its operands — `a + b` calls `a.__add__(b)` (falling back to `b.__radd__(a)`). Operators are grouped by role: arithmetic, comparison, logical, bitwise, assignment, identity, membership, and a few specialised forms (ternary, unpacking, walrus). Precedence and associativity determine how expressions parse.

## Arithmetic
| Op   | Meaning        | Example         |
|------|----------------|-----------------|
| `+`  | add            | `2 + 3 → 5`     |
| `-`  | subtract       | `5 - 3 → 2`     |
| `*`  | multiply       | `2 * 3 → 6`     |
| `/`  | true division  | `15 / 4 → 3.75` |
| `//` | floor division | `15 // 4 → 3`   |
| `%`  | modulo         | `15 % 4 → 3`    |
| `**` | exponentiation | `3 ** 3 → 27`   |

`//` rounds toward **negative infinity**, not toward zero. `%` has the sign of the divisor. The identity `a == (a // b) * b + (a % b)` always holds.
```python
-7 // 2                 # -4  (not -3)
-7 %  2                 # 1   (not -1)
divmod(-7, 2)           # (-4, 1)
```

`divmod(a, b)` returns `(a // b, a % b)` in one call.

## Comparison
`<  <=  >  >=  ==  !=` — return `bool`. Chained comparisons desugar into `and`:
```python
1 < x < 10              # (1 < x) and (x < 10) — x evaluated once
a == b == c             # (a == b) and (b == c)
```

## Logical
`and`, `or`, `not` short-circuit and **return an operand**, not a coerced `bool`.
```python
0 or "hi"               # 'hi'
"a" and "b"             # 'b'
None or []              # []
not 0                   # True
```

Common idiom: `name = user_input or "default"`.

## Bitwise
| Op   | Meaning     |
|------|-------------|
| `&`  | AND         |
| `\|` | OR          |
| `^`  | XOR         |
| `~`  | NOT         |
| `<<` | left shift  |
| `>>` | right shift |

`~x == -(x + 1)` — two's-complement on arbitrary-precision ints.

## Assignment
Simple: `=`. Augmented: `+= -= *= /= //= %= **= <<= >>= &= |= ^=`. Augmented forms call `__iadd__` etc. on mutables (in-place) or rebind on immutables.

## Identity
`is`, `is not` — same object (`id(x) == id(y)`). Reserved for singletons: `None`, `True`, `False`, sentinel objects.
```python
if x is None: ...
if result is _MISSING: ...
```

Never use `is` to compare values — `a = 1000; b = 1000; a is b` is implementation-defined.

## Membership
`in`, `not in` — dispatches to `__contains__`, or iterates via `__iter__`. O(1) for `set`/`dict` (hash lookup), O(n) for `list`/`tuple`/`str` (linear scan; substring for `str`).
```python
3 in [1, 2, 3]          # True
"ab" in "abc"           # True — substring, not element
"a" in {"a": 1}         # True — checks keys
```

## Ternary
```python
value = a if cond else b
```
Right-associative: `a if p else b if q else c` parses as `a if p else (b if q else c)`.

## Unpacking `*` / `**`
In **calls**, spread iterables and mappings:
```python
f(*args, **kwargs)
```

In **assignment targets**, capture a slice into a list:
```python
first, *rest = [1, 2, 3, 4]     # first=1, rest=[2,3,4]
```

In **literals**, splice one collection into another:
```python
[1, *[2, 3], 4]                 # [1, 2, 3, 4]
{**a, **b}                      # merge two dicts (b wins on conflict)
```

## Walrus `:=`
Named expression — binds and yields the value in place.
```python
while (line := f.readline()):
    process(line)

if (n := len(data)) > 10:
    print(f"too long: {n}")
```

## Precedence (high → low)
```
**                      right-associative
unary  +  -  ~
*  /  //  %  @
+  -
<<  >>
&
^
|
in  not in  is  is not  <  <=  >  >=  !=  ==
not
and
or
if – else               (ternary)
lambda
:=                      (walrus)
```

`**` is right-associative: `2 ** 3 ** 2 == 2 ** (3 ** 2) == 512`. Bitwise `& ^ |` are three separate tiers — `5 | 1 ^ 4` parses as `5 | (1 ^ 4)` → `5`.

## Gotchas
- **`is` vs `==` due to interning** — small ints (`-5..256`) and short strings are cached, so `a is b` may look correct. It isn't. Use `==`.
- **`not x == y` parses as `not (x == y)`** — `not` has lower precedence than `==`.
- **`not x in y` parses as `not (x in y)`** — write `x not in y` for clarity.
- **`-2 ** 2 == -4`** — `**` binds tighter than unary minus. Use `(-2) ** 2`.
- **`a < b < c` evaluates `b` once** — but `a < f() < c` still calls `f()` once. Don't refactor to `a < b and b < c` if `b` has side effects.
- **`and`/`or` return operands, not `bool`** — `[] or None` is `None`; `1 and 2` is `2`. Wrap in `bool(...)` if you need a boolean.
- **Augmented assignment on shared mutables** — `a = b = []; a += [1]` mutates the shared list; `b` also sees `[1]`.
