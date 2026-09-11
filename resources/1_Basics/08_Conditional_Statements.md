# Conditional Statements

Source: `src/1_Basics/6_Conditional.py`

## Definition
Conditional statements let a program choose which code to run.

They are based on conditions that evaluate to `True` or `False`.

## The `if` Statement
Use `if` to run code only when a condition is true.

```python
age = 20

if age >= 18:
    print("Adult")
```

The indented line runs only if `age >= 18` is true.

## The `else` Statement
Use `else` for the alternative case.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Only one branch runs.

## The `elif` Statement
Use `elif` for more than two choices.

```python
age = 25

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young adult")
else:
    print("Adult")
```

Python checks the conditions from top to bottom.

The first true branch runs, and the rest are skipped.

## Condition Order
Order matters when conditions overlap.

```python
score = 95

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

Put the most specific or highest-priority condition first.

## Indentation
Python uses indentation to define blocks.

```python
if age >= 18:
    print("Adult")
    print("Can vote")

print("Done")
```

The first two `print()` calls belong to the `if` block. The last one does not.

## Conditional Expressions
A conditional expression chooses one value from two options.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

Format:

```python
value_if_true if condition else value_if_false
```

Use it for short expressions only.

## `match` and `case`
Python 3.10 added pattern matching.

```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not found")
    case _:
        print("Other")
```

`case _` is the default case.

## Common Conditions
| Expression | Meaning |
|------------|---------|
| `x == y` | values are equal |
| `x != y` | values are not equal |
| `x > y` | x is greater than y |
| `x >= y` | x is greater than or equal to y |
| `x in items` | x exists in items |
| `x is None` | x is exactly `None` |

## Common Mistakes
- Using `=` instead of `==`.
- Forgetting the colon after `if`, `elif`, or `else`.
- Using wrong indentation.
- Putting a broad condition before a specific one.
- Using a conditional expression for complicated logic.

## Summary
- Use `if` to run code when a condition is true.
- Use `else` for the alternative.
- Use `elif` for extra branches.
- Indentation controls the block.
- Use `match` and `case` for pattern-style branching in Python 3.10+.
