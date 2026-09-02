# Conditional Statements

Source: `src/1_Basics/6_Conditional.py`

## Definition
Conditional statements choose which block of code runs based on a boolean condition.

## `if`, `elif`, `else`
```python
age = 25

if age <= 12:
    print("Kid")
elif age <= 19:
    print("teenager")
elif age <= 35:
    print("Young adult")
else:
    print("Adult")
```

Python checks conditions from top to bottom. The first true branch runs, and the rest are skipped.

## Condition order matters
For age ranges, start with the smallest upper bound when using `<=`.
```python
if age <= 12:
    ...
elif age <= 19:
    ...
```

If a broad condition appears first, it can block later conditions.

## Indentation
Python uses indentation to define blocks.
```python
if age >= 18:
    print("Adult")
    print("Can vote")
```

Both indented lines belong to the `if` block.

## Ternary operator
Use a conditional expression for simple value selection.
```python
age = 19
voter = "Adult" if age >= 18 else "Minor"
print(voter)
```

Format:
```python
value_if_true if condition else value_if_false
```

Use this only for short expressions. Use normal `if` / `else` blocks when logic becomes larger.

## `match` / `case`
Pattern matching is available in Python 3.10 and newer.
```python
number = 1

match number:
    case 1:
        print("one")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
```

`case _` is the default case.

## Common comparison expressions
| Expression | Meaning |
|------------|---------|
| `age >= 18` | age is at least 18 |
| `age <= 12` | age is at most 12 |
| `x == y` | values are equal |
| `x != y` | values are not equal |
| `x in values` | value exists in a container |

## Gotchas
- **Use `==` for equality**, not `=`.
- **Indentation is syntax** in Python.
- **Branch order matters** when conditions overlap.
- **The ternary operator is for expressions**, not multi-line logic.
- **`match` / `case` requires Python 3.10+**.
