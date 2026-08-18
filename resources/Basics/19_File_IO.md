# File I/O

## What is file I/O?
File I/O means **reading from** and **writing to** files on your computer. In Python you use `open()` to open a file, then call `.read()` or `.write()`. Always wrap it in `with open(...) as f:` so Python closes the file automatically.

## Opening a file
```python
with open("data.txt") as f:
    contents = f.read()
```
`open(path, mode="r", encoding=None)` — text mode by default. Always specify `encoding` for text files if portability matters.
```python
with open("data.txt", encoding="utf-8") as f:
    ...
```

## Modes
| Mode | Meaning |
|------|---------|
| `"r"` | read (default) — file must exist |
| `"w"` | write — **truncates** the file if it exists, creates it if not |
| `"a"` | append — writes at end of file, creates if missing |
| `"x"` | exclusive create — fails if the file exists |
| `"r+"` | read + write; file must exist |
| `"b"` | binary suffix — `"rb"`, `"wb"`, `"ab"` — reads/writes `bytes`, not `str` |
| `"t"` | text suffix (default) — reads/writes `str` |

Modes combine: `"rb"`, `"w+b"`, etc.

## Reading
```python
with open("data.txt", encoding="utf-8") as f:
    text = f.read()                 # whole file as one string
```
```python
with open("data.txt", encoding="utf-8") as f:
    line = f.readline()             # one line, including trailing \n
```
```python
with open("data.txt", encoding="utf-8") as f:
    for line in f:                  # iterate line by line — memory-friendly
        print(line.rstrip())        # strip trailing \n
```
```python
with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()           # list of all lines
```
Prefer the loop for large files — `read()` and `readlines()` load everything into memory.

## Writing
```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
    f.write("world\n")
```
`write` does **not** add a newline — include `\n` yourself.
```python
lines = ["a\n", "b\n", "c\n"]
with open("out.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)             # no \n added — content is written verbatim
```

## Appending
```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("new entry\n")
```

## Binary I/O
For images, PDFs, pickled data — anything that isn't text.
```python
with open("photo.jpg", "rb") as f:
    data = f.read()                 # bytes, not str

with open("copy.jpg", "wb") as f:
    f.write(data)
```

## Position — `tell` and `seek`
```python
with open("data.txt", encoding="utf-8") as f:
    f.read(5)
    f.tell()                        # current byte offset
    f.seek(0)                       # rewind to start
```
`seek(offset, whence)` — `whence`: `0` (start, default), `1` (current), `2` (end). Only `0` is portable in text mode.

## Line endings and encoding
- Python normalizes line endings by default: reads translate `\r\n` → `\n`; writes translate `\n` → OS newline. Pass `newline=""` to disable (needed for `csv` and binary-ish text).
- Always pass `encoding=` for text files. The default is platform-dependent and has burned many people on Windows.

## Working with paths — `pathlib`
The modern idiom. Cleaner than `os.path`, and file objects accept `Path` instances.
```python
from pathlib import Path

p = Path("data") / "input.txt"
p.exists()
text = p.read_text(encoding="utf-8")            # one-shot read
p.write_text("hello\n", encoding="utf-8")       # one-shot write

for csv in Path("data").glob("*.csv"):
    print(csv.name)
```

## Common patterns
Reading JSON:
```python
import json
with open("config.json", encoding="utf-8") as f:
    config = json.load(f)
```
Reading CSV:
```python
import csv
with open("data.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## Gotchas
- **`"w"` truncates** — opening in write mode deletes the file's contents immediately, even if you never call `write`.
- **Always specify `encoding`** for text mode. The default varies by OS/locale.
- **`write` doesn't add newlines** — you must include `\n` yourself. Neither does `writelines`.
- **Binary vs text mode** is not just about content — `read` returns `bytes` in binary mode and `str` in text mode. Trying to `write` a `str` to a `"wb"` file raises `TypeError`.
- **Iterating a file is one-shot** — after the loop finishes, `seek(0)` before iterating again.
- **Don't forget `with`** — a manually opened file that isn't closed can leak resources or corrupt data (writes may not flush).
- **`newline=""`** — pass this when reading/writing CSVs, or you'll get blank rows on Windows.
