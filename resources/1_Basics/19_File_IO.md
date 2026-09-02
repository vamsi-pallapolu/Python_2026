# File I/O

Source: `src/1_Basics/10_Files/1_open.py`

## Definition
File I/O means reading from and writing to files. Python's built-in `open()` returns a file object.

The source file uses `pathlib.Path` to build paths relative to the Python file.

## Building file paths with `pathlib`
```python
from pathlib import Path

current_file = Path(__file__)
print(f"Current file path:{current_file}")

current_dir = Path(__file__).resolve().parent
data_file = current_dir / "data_file1.txt"
```

`Path(__file__)` represents the current Python file. `.resolve().parent` gives the directory that contains it.

Use `/` with `Path` objects to join path parts.

## Opening a file for writing
```python
try:
    file = open(data_file, "w")
except FileNotFoundError as e:
    print("Error occured while opening the file:", e)
finally:
    file.close()
```

Mode `"w"` opens a file for writing. It creates the file if needed and truncates the file if it already exists.

## Common file modes
| Mode | Meaning |
|------|---------|
| `"r"` | read; file must exist |
| `"w"` | write; create or truncate |
| `"a"` | append; create if missing |
| `"x"` | create; fail if file exists |
| `"rb"` | read binary |
| `"wb"` | write binary |

## Reading a file
```python
data_file = current_dir / "data_file.txt"

try:
    file = open(data_file, "r")
    data = file.read()
    print(f"Type of data:{type(data)}")
    for line in data:
        print(line, end="")
    print()
except FileNotFoundError as e:
    print(e)
finally:
    file.close()
```

`read()` returns the full file contents as one string in text mode.

Note that looping over `data` loops character by character because `data` is a string.

For line-by-line reading, loop over the file object:
```python
with open(data_file, "r") as file:
    for line in file:
        print(line, end="")
```

## Appending to a file
```python
data_file = current_dir / "append_file.txt"

try:
    file = open(data_file, "a")
    file.write("Appending a line\n")
    file.write("Appendinf another line")
except FileNotFoundError as e:
    print(e)
```

Mode `"a"` writes at the end of the file. `write()` does not add a newline automatically.

## Closing files
Files should be closed after use.
```python
file.close()
```

The preferred pattern is a `with` block:
```python
with open(data_file, "r") as file:
    for char in file.read():
        print(char, end="")
```

The file closes automatically when the `with` block exits.

## Safer version
```python
from pathlib import Path

current_dir = Path(__file__).resolve().parent
data_file = current_dir / "data_file.txt"

try:
    with open(data_file, "r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError as e:
    print(e)
else:
    print(data)
```

Passing `encoding="utf-8"` makes text behavior more predictable across operating systems.

## Gotchas
- **Mode `"w"` truncates existing files**.
- **Mode `"a"` appends to the end**.
- **`read()` returns a string in text mode**.
- **Looping over a string gives characters**, not lines.
- **`write()` does not add newlines**.
- **Use `with open(...)`** so files close automatically.
- **Pass `encoding="utf-8"`** for text files.
