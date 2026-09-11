# Input / Output

Source: `src/1_Basics/1_io.py`

## Definition
Input/output is how a program receives data and shows results.

In basic Python programs:

- `input()` reads text from the user
- `print()` displays output

## Printing Output
Use `print()` to show values.

```python
print("Hello")
print(10)
print(2 + 3)
```

`print()` can show multiple values.

```python
name = "Vamsi"
age = 25

print(name, age)
```

Output:

```text
Vamsi 25
```

By default, `print()` adds a space between values and a newline at the end.

## Reading Input
Use `input()` to read from the keyboard.

```python
name = input("Enter your name: ")
print("Hello", name)
```

The text inside `input()` is the prompt shown to the user.

## Input Is Always a String
`input()` always returns a string.

```python
age = input("Enter your age: ")
print(type(age))
```

Even if the user types `25`, the value is `"25"`, not the integer `25`.

Convert it before doing math.

```python
age = int(input("Enter your age: "))
print(age + 1)
```

## Common Conversions
| Function | Example | Result |
|----------|---------|--------|
| `str(x)` | `str(10)` | `"10"` |
| `int(x)` | `int("10")` | `10` |
| `float(x)` | `float("3.5")` | `3.5` |

## F-Strings
F-strings are a clear way to place values inside strings.

```python
name = "Vamsi"
age = 25

print(f"{name} is {age} years old")
```

Output:

```text
Vamsi is 25 years old
```

## Reading Multiple Values
Use `.split()` to split one line into pieces.

```python
x, y = input("Enter two numbers: ").split()

print(x)
print(y)
```

If the user enters:

```text
10 20
```

Then `x` is `"10"` and `y` is `"20"`.

Convert them if needed:

```python
x, y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)

print(x + y)
```

## Handling Invalid Input
Numeric conversion can fail.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a valid number")
```

Use `try` and `except` when user input may be invalid.

## Common Mistakes
- Forgetting that `input()` returns a string.
- Trying to do math before converting input.
- Forgetting spaces in prompts, such as `"Name:"` instead of `"Name: "`.
- Using `.split()` and giving too many or too few values.
- Forgetting that `print()` adds a newline by default.

## Summary
- Use `print()` to display output.
- Use `input()` to read text from the user.
- Convert input with `int()` or `float()` before numeric operations.
- Use f-strings for readable output.
