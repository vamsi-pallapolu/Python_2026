# Operators

Source: `Basics/3_operators.py`

## What is an operator?
An operator is a **symbol that does something with values** — like `+` for adding, `==` for checking equality, `and` for combining conditions. Python groups them into arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators.

## Arithmetic
| Op   | Meaning        | Example       |
|------|----------------|---------------|
| `+`  | add            | `2 + 3 → 5`   |
| `-`  | subtract       | `5 - 3 → 2`   |
| `*`  | multiply       | `2 * 3 → 6`   |
| `/`  | true division  | `15/4 → 3.75` |
| `//` | floor division | `15//4 → 3`   |
| `%`  | modulus        | `15%4 → 3`    |
| `**` | exponentiation | `3**3 → 27`   |

## Comparison (relational)
`<  <=  >  >=  ==  !=` — result is `True` or `False`.

## Logical
`and`, `or`, `not` — with **short-circuit** evaluation.
```python
True and False   # False
True or False    # True
not False        # True
```

## Bitwise
| Op   | Meaning     |
|------|-------------|
| `&`  | AND         |
| `\|` | OR          |
| `^`  | XOR         |
| `~`  | NOT         |
| `<<` | left shift  |
| `>>` | right shift |

## Assignment (compound)
`= += -= *= /= //= %= **= <<= >>= &= |= ^=`

## Identity
Check whether two names refer to the **same object**.
```python
a = 10
b = 20
c = a
a is c        # True
a is not b    # True (different objects)
```

## Membership
Test whether a value is in a sequence.
```python
x in my_list
x not in "hello"
```

## Ternary (conditional expression)
```python
min_ = a if a < b else b
```

## Operator precedence & associativity
Higher precedence binds tighter. Rough order (high → low):

`**`  →  unary `+ - ~`  →  `* / // %`  →  `+ -`  →  shifts  →  `&`  →  `^`  →  `|`  →  comparisons  →  `not`  →  `and`  →  `or`.

> Bitwise `&`, `^`, `|` are **three separate tiers** — `&` binds tighter than `^`, which binds tighter than `|`. So `5 | 1 ^ 4` parses as `5 | (1 ^ 4)` → `5 | 5` → `5`.

- `**` is **right-associative**: `2**3**2 == 2**(3**2) == 512`.
- Most others are left-associative.
- Use parentheses when clarity matters.
