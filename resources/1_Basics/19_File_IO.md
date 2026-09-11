# File I/O

Source: `src/1_Basics/10_Files/1_open.py`

## Definition
File I/O means reading from and writing to files.

Python uses `open()` to open files.

```python
file = open("data.txt")
```

Most of the time, you should open files with `with`.

```python
with open("data.txt") as file:
    data = file.read()
```

The file closes automatically when the `with` block ends.

## File Paths
Use `pathlib.Path` to work with file paths.

```python
from pathlib import Path

current_dir = Path(__file__).resolve().parent
data_file = current_dir / "data.txt"
```

`Path(__file__)` represents the current Python file.

`.parent` gets the folder containing the file.

The `/` operator joins path parts.

## Opening Files
Use `open(path, mode)` to open a file.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The mode tells Python what you want to do.

## Common File Modes
| Mode | Meaning |
|------|---------|
| `"r"` | read text; file must exist |
| `"w"` | write text; create or replace |
| `"a"` | append text; create if missing |
| `"x"` | create text; fail if file exists |
| `"rb"` | read binary |
| `"wb"` | write binary |

## Reading a Whole File
Use `.read()` to read the whole file as one string.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(data)
```

Use this when the file is small enough to fit comfortably in memory.

## Reading Line by Line
Loop over the file object to read one line at a time.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

Each `line` includes the newline character at the end, unless it is the last line and the file does not end with one.

Use `.strip()` to remove surrounding whitespace.

```python
clean_line = line.strip()
```

## Writing to a File
Use mode `"w"` to write.

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello\n")
    file.write("World\n")
```

`write()` does not add a newline automatically.

Mode `"w"` replaces the existing file contents.

## Appending to a File
Use mode `"a"` to add to the end of a file.

```python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Program started\n")
```

Appending keeps the existing content.

## Handling Missing Files
Reading a missing file raises `FileNotFoundError`.

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
```

## Text and Binary Files
Text mode works with strings.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

Binary mode works with bytes.

```python
with open("image.png", "rb") as file:
    data = file.read()
```

Use binary mode for images, PDFs, audio files, and other non-text data.

## Common Mistakes
- Forgetting to close a file. Use `with`.
- Using mode `"w"` and accidentally replacing a file.
- Forgetting that `write()` does not add newlines.
- Looping over a string from `.read()` and expecting lines.
- Not passing `encoding="utf-8"` for text files.
- Reading a very large file all at once.

## Summary
- Use `open()` to work with files.
- Prefer `with open(...)` so files close automatically.
- Use `"r"` to read, `"w"` to write, and `"a"` to append.
- Use `encoding="utf-8"` for text files.
- Loop over the file object for line-by-line reading.
