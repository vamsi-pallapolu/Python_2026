# Operators

Source: `src/1_Basics/3_operators.py`

## Definition
Operators are symbols or keywords that perform operations on values.

## Arithmetic operators
```python
a = 15
b = 4

print(a / b)      # division: 3.75
print(a // b)     # floor division: 3
print(a % b)      # modulus: 3
print(3 ** 3)     # exponentiation: 27
```

| Operator | Meaning |
|----------|---------|
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division |
| `//` | floor division |
| `%` | remainder |
| `**` | exponentiation |

## Comparison operators
Comparison operators return booleans.
```python
a = 13
b = 12

print(a < b)      # False
print(a == b)     # False
print(a >= b)     # True
```

| Operator | Meaning |
|----------|---------|
| `<` | less than |
| `<=` | less than or equal |
| `>` | greater than |
| `>=` | greater than or equal |
| `==` | equal value |
| `!=` | not equal value |

## Logical operators
```python
a = True
b = False

print(a and b)    # False
print(a or b)     # True
print(not b)      # True
```

| Operator | Meaning |
|----------|---------|
| `and` | true when both sides are true |
| `or` | true when at least one side is true |
| `not` | reverses truth value |

## Bitwise operators
Bitwise operators work on integer bits.
```python
5 & 3     # 1
5 | 3     # 7
5 ^ 3     # 6
~5        # -6
5 << 1    # 10
5 >> 1    # 2
```

| Operator | Meaning |
|----------|---------|
| `&` | bitwise AND |
| `|` | bitwise OR |
| `^` | bitwise XOR |
| `~` | bitwise NOT |
| `<<` | left shift |
| `>>` | right shift |

## Assignment operators
```python
x = 10
x += 5      # same as x = x + 5
x -= 2
x *= 3
x /= 2
x <<= 1
```

Assignment operators update the variable binding or mutate the target depending on the object and operation.

## Identity operators
Identity checks whether two names refer to the same object.
```python
a = 10
b = 20
c = a

print(a is not b)      # True
print(a is c)          # True
```

Use `==` for value comparison. Use `is` mainly for identity checks such as `x is None`.

## Membership operators
Membership checks whether a value exists inside a container.
```python
x = 24
my_list = [10, 20, 30, 40]

if x in my_list:
    print("found")
else:
    print("not found")
```

Operators:
| Operator | Meaning |
|----------|---------|
| `in` | value exists in container |
| `not in` | value does not exist in container |

## Ternary operator
Python's conditional expression selects one of two values.
```python
a, b = 10, 20
minimum = a if a < b else b
print(minimum)         # 10
```

Format:
```python
value_if_true if condition else value_if_false
```

## Precedence and associativity
Operator precedence decides which operation runs first.
```python
2 ** 3 ** 2      # 512
```

Exponentiation is right-associative:
```python
2 ** (3 ** 2)
```

Use parentheses when readability matters.

## Gotchas
- **`/` always returns a float**.
- **`//` floors the result**, which matters for negative numbers.
- **`==` compares values; `is` compares identity**.
- **Do not name variables `min` or `list`** because that shadows built-ins.
- **Use parentheses** when an expression mixes several operator groups.
