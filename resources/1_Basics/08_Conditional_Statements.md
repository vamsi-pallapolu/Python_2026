# Conditional Statements

Source: `Basics/6_Conditional.py`

## Definition
A conditional statement selects one of several branches based on the truthiness of one or more expressions. Python provides `if / elif / else` (linear branching), the ternary conditional expression `x if cond else y` (branching inside an expression), and `match / case` (structural pattern matching, 3.10+). Blocks are delimited by **indentation**, not braces.

## `if / elif / else`
The interpreter evaluates each condition top-to-bottom; the **first truthy** branch runs and the rest are skipped.

```python
if age <= 12:
    print("Kid")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young adult")
else:
    print("Adult")
```

- Each branch is a block delimited by indentation (4 spaces by PEP 8).
- `elif` is a single token; there is no `else if`.
- `else` is optional; without it and with no match, no branch runs.

## Short-circuit chain evaluation
Only the conditions up to the first true one are evaluated. Conditions after that are not touched — safe for guarded checks.

```python
if user is not None and user.is_admin:      # user.is_admin never evaluated when user is None
    ...
```

## Ternary conditional expression
An expression (not a statement) that returns one of two values. Evaluation order is `cond → true_branch` or `cond → false_branch`.

```python
voter = "Adult" if age >= 18 else "Minor"
label = "even" if n % 2 == 0 else "odd"
```

Binds loosely — parenthesize when nesting or combining with other operators.

```python
score = (100 if perfect else 50) + bonus                # parens for clarity
tier  = "A" if s >= 90 else "B" if s >= 75 else "C"     # right-associative chain
```

## Guard-clause style
Prefer early exits over deep nesting. Flat is easier to read and easier to reason about.

```python
def process(user):
    if user is None:
        return
    if not user.active:
        return
    ...             # main path, un-indented
```

## `match / case` (3.10+)
Structural pattern matching. Each `case` is a **pattern**, not just an expression — patterns can destructure, capture, and match by shape.

```python
match command.split():
    case ["quit"]:                 print("bye")
    case ["load", path]:           load(path)                # captures 'path'
    case ["save", *rest]:          save(rest)                # sequence + splat
    case _:                        print("unknown")          # wildcard
```

### Literal and OR patterns
```python
match status:
    case 200 | 201 | 204:   print("ok")
    case 404:               print("not found")
    case _:                 print("other")
```

### Capture patterns and the bare-name pitfall
A **bare name** in a pattern binds a new variable — it does not compare against an existing one. A **dotted name** compares by equality.

```python
FORBIDDEN = 42

match n:
    case FORBIDDEN:         # BUG — this binds a new local FORBIDDEN, matches anything
        print("blocked")

match n:
    case consts.FORBIDDEN:  # OK — dotted name compares by value
        print("blocked")
    case 42:                # OK — literal
        print("blocked")
```

### Class patterns
Match by type and attribute; keyword arguments compare, bare names capture.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

match p:
    case Point(x=0, y=0):       print("origin")
    case Point(x=0, y=y):       print(f"on Y at {y}")     # captures y
    case Point(x=x, y=y):       print(f"({x}, {y})")
```

### Mapping and sequence patterns
```python
match event:
    case {"type": "click", "x": x, "y": y}:  handle_click(x, y)
    case {"type": "key", **rest}:            handle_key(rest)     # **rest captures remainder

match seq:
    case []:              print("empty")
    case [x]:             print("one", x)
    case [x, *rest]:      print("head", x, "tail", rest)
```

### Guards
Add a boolean condition on top of the pattern with `if`.

```python
match point:
    case (x, y) if x == y:   print("diagonal")
    case (x, y) if x > 0:    print("positive x")
    case (x, y):             print("other")
```

## Gotchas
- **Indentation must be consistent** — mixing tabs and spaces raises `TabError`. Stick to spaces (PEP 8: 4).
- **`is` vs `==` in conditions** — `is` compares identity, `==` compares value. Use `is` only for singletons (`None`, `True`, `False`). `if x is 1000:` may be `False` even when `x == 1000`.
- **`match` bare names capture, don't compare** — a lone `case NAME:` matches everything and rebinds `NAME`. Use dotted names, literals, or a guard (`case n if n == NAME:`).
- **Ternary precedence** — `x = a if cond else b + c` parses as `x = a if cond else (b + c)`. Parenthesize when in doubt.
- **`elif` chains vs multiple `if`s** — separate `if` statements evaluate every condition and can run more than one block; an `elif` chain runs at most one.
- **No fall-through in `match`** — once a case matches, control leaves the `match`. There is no `switch`-style fall-through.
