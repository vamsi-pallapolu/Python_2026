# Conditional Statements

Source: `Basics/6_Conditional.py`

## `if / elif / else`
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
- Blocks are defined by **indentation** (4 spaces by convention).
- `elif` is short for "else if"; you can chain as many as you need.
- `else` is optional.

## Ternary form (conditional expression)
```python
voter = "Adult" if age >= 18 else "Minor"
```

## Truthiness
Falsy values (evaluate to `False` in a boolean context):
`False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`.
Everything else is **truthy**.

```python
if items:               # runs when items is non-empty
    ...
```

## Nested conditions
```python
if logged_in:
    if is_admin:
        show_admin_panel()
    else:
        show_user_panel()
```

## `match` / `case` — Python 3.10+
Structural pattern matching, similar to `switch` in other languages.
```python
match number:
    case 1:
        print("one")
    case 2 | 3:                # OR pattern
        print("Two or Three")
    case _:                    # wildcard (default)
        print("Other number")
```
Patterns can also destructure:
```python
match point:
    case (0, 0):        print("Origin")
    case (x, 0):        print(f"On X-axis at {x}")
    case (0, y):        print(f"On Y-axis at {y}")
    case (x, y):        print(f"({x}, {y})")
```
