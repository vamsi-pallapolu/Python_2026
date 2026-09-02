# Input / Output

Source: `src/1_Basics/1_io.py`

## Definition
Input/output is how a program receives data and shows results. In Python, the basic tools are:

- `input()` to read text from the user
- `print()` to display output

`input()` always returns a string, even when the user types a number.

## Reading one value
```python
name = input("Enter name:")
print(f"Hello, {name}")
```

The prompt is shown first. After the user presses Enter, the typed text is stored in `name`.

## Printing values
```python
name = "vamsi"
age = 25
city = "NewYork"

print(name, age, city)
```

`print()` can receive multiple values. By default, it separates them with a space and ends with a newline.

## F-strings
F-strings are the preferred way to format values inside strings.
```python
name = "vamsi"
print(f"Hello, {name}")
```

The expression inside `{}` is evaluated and inserted into the string.

## Reading multiple values
Use `.split()` to separate one input line into multiple parts.
```python
x, y = input("Enter numbers").split()
print(x, y)
```

If the user types:
```text
10 20
```

Then:
```python
x == "10"
y == "20"
```

Both values are still strings.

## Type conversion
Convert input when numeric operations are needed.
```python
i = int(input("How old are you?"))
f = float(input("Evaluate 7/2 :"))

print("Age:", i)
print(f)
```

Common conversions:
| Function | Converts to |
|----------|-------------|
| `str(x)` | string |
| `int(x)` | integer |
| `float(x)` | floating-point number |

## Handling invalid numeric input
`int()` and `float()` raise `ValueError` if the text cannot be converted.
```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a valid number")
```

## Gotchas
- **`input()` returns `str`** - convert explicitly before math.
- **`.split()` splits on whitespace by default**.
- **Unpacking must match the number of inputs** - `x, y = input().split()` needs exactly two values.
- **Use f-strings for readable output**.
- **Numeric conversion can fail** - use `try` / `except` for real user input.
