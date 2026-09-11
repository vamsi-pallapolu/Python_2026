# Operators

Source: `src/1_Basics/3_operators.py`

## Definition
Operators are symbols or keywords that perform operations on values.

```python
print(2 + 3)
print(10 > 5)
```

## Arithmetic Operators
Arithmetic operators work with numbers.

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | addition | `2 + 3` |
| `-` | subtraction | `5 - 2` |
| `*` | multiplication | `4 * 3` |
| `/` | division | `10 / 4` |
| `//` | floor division | `10 // 4` |
| `%` | remainder | `10 % 4` |
| `**` | power | `2 ** 3` |

```python
a = 15
b = 4

print(a / b)
print(a // b)
print(a % b)
print(2 ** 3)
```

Output:

```text
3.75
3
3
8
```

## Comparison Operators
Comparison operators return `True` or `False`.

| Operator | Meaning |
|----------|---------|
| `==` | equal |
| `!=` | not equal |
| `<` | less than |
| `<=` | less than or equal |
| `>` | greater than |
| `>=` | greater than or equal |

```python
age = 20

print(age >= 18)
print(age == 21)
```

## Logical Operators
Logical operators combine conditions.

| Operator | Meaning |
|----------|---------|
| `and` | true when both sides are true |
| `or` | true when at least one side is true |
| `not` | reverses a condition |

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

## Assignment Operators
Assignment operators update a variable.

```python
x = 10
x += 5
x -= 2
x *= 3
```

`x += 5` means:

```python
x = x + 5
```

## Identity Operators
Identity operators check whether two names refer to the same object.

| Operator | Meaning |
|----------|---------|
| `is` | same object |
| `is not` | not the same object |

```python
value = None

if value is None:
    print("missing")
```

Use `==` for normal value comparison.

## Membership Operators
Membership operators check whether a value exists in a container.

| Operator | Meaning |
|----------|---------|
| `in` | exists inside |
| `not in` | does not exist inside |

```python
names = ["Asha", "Ben"]

if "Asha" in names:
    print("found")
```

## Conditional Expression
A conditional expression chooses one of two values.

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

Format:

```python
value_if_true if condition else value_if_false
```

Use it for short, simple choices.

## Operator Precedence
Precedence decides which operation happens first.

```python
print(2 + 3 * 4)
```

Output:

```text
14
```

Multiplication happens before addition.

Use parentheses when it helps readability.

```python
print((2 + 3) * 4)
```

## Common Mistakes
- Using `=` when you mean `==`.
- Using `is` for normal value comparison.
- Forgetting that `/` returns a float.
- Forgetting that `//` means floor division.
- Writing long expressions without parentheses.

## Summary
- Operators perform operations on values.
- Arithmetic operators do math.
- Comparison operators return booleans.
- Logical operators combine conditions.
- Use `==` for equality and `is` mostly for `None`.
