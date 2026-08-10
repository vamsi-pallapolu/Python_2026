# Input / Output

Source: `Basics/1_io.py`

## What is I/O?
Input/Output is how a program communicates with the outside world — reading data from a source (keyboard, file, network) and writing results back to a destination (screen, file, network). In Python, the two built-ins `input()` and `print()` cover standard console I/O.

## `print()`
- Writes to standard output.
- Multiple args are separated by a space by default: `print(a, b, c)`.
- Useful keyword args:
  - `sep=","` — separator between arguments.
  - `end="\n"` — what to append at the end (default newline).

```python
print("Hello", "World")            # Hello World
print("Hello", "World", sep="-")   # Hello-World
print("no newline", end="")
```

## `input()`
- Reads a line from standard input.
- Always returns a **string** — convert as needed.

```python
name = input("Enter name: ")
age  = int(input("How old are you? "))
f    = float(input("Evaluate 7/2: "))
```

## Reading multiple values on one line
```python
x, y = input("Enter numbers: ").split()       # both are strings
a, b = map(int, input().split())              # both are ints
```

## f-strings (formatted string literals)
```python
name = "Vamsi"
print(f"Hello, {name}")
print(f"{3.14159:.2f}")   # 3.14
```

## Other formatting options
```python
"Hello, {}".format(name)   # str.format
"Hello, %s" % name         # old-style
```

## Notes
- `input()` blocks until the user hits Enter.
- Wrap conversion in `try/except ValueError` when the input might not be numeric.
