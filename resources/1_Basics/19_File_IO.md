# File I/O

## Definition
File I/O is reading from and writing to files through file objects. The entry point is `open(path, mode="r", encoding=None, newline=None)`, which returns a file object. Use it inside a `with` block so the file is closed deterministically when the block exits — including on exception.
```python
with open("data.txt", encoding="utf-8") as f:
    text = f.read()
```

## Modes
| Mode | Effect |
|------|--------|
| `"r"` | read (default); file must exist |
| `"w"` | write; **truncates** to zero length or creates |
| `"a"` | append; writes always go to end; creates if missing |
| `"x"` | exclusive create; raises `FileExistsError` if the file exists |
| `"r+"` | read + write, positioned at 0; file must exist |
| `"w+"` | read + write, truncates first |
| `"b"` | binary suffix — `rb`, `wb`, `ab` — I/O in `bytes` |
| `"t"` | text suffix (default) — I/O in `str` |

Modes combine: `"rb"`, `"w+b"`, `"xt"`.

## Text vs binary
- Text mode returns `str`. The file object decodes bytes using `encoding` and translates line endings.
- Binary mode returns `bytes`. No decoding, no newline translation.

Writing a `str` to a binary file (or `bytes` to a text file) raises `TypeError`.

## Encoding
Always pass `encoding="utf-8"` for text. The default (`locale.getencoding()`) is platform-dependent — on Windows it can be `cp1252`, which corrupts non-ASCII silently.

`errors=` controls decode failures:
- `"strict"` (default) — raise `UnicodeDecodeError`.
- `"replace"` — insert `U+FFFD` for undecodable bytes.
- `"ignore"` — drop them.
- `"surrogateescape"` — round-trip undecodable bytes as surrogate code points (useful when re-emitting).

## Newlines
Text mode translates newlines by default: reads collapse `\r\n` → `\n`; writes translate `\n` → OS newline. Pass `newline=""` to disable translation. Required for the `csv` module.

## Reading
```python
with open("data.txt", encoding="utf-8") as f:
    text = f.read()             # entire file → str
    # or
    line = f.readline()         # one line, includes trailing "\n"
    # or
    lines = f.readlines()       # list[str] of all lines
```
Iterate for memory-friendly line-by-line reads (buffered internally):
```python
with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))
```

## Writing
```python
with open("out.txt", "w", encoding="utf-8") as f:
    n = f.write("hello\n")      # returns number of chars written
    f.writelines(["a\n", "b\n"])  # no separator added
```
Neither `write` nor `writelines` appends a newline — include `\n` in the strings.

## Binary I/O
```python
with open("photo.jpg", "rb") as f:
    data = f.read()             # bytes

with open("copy.jpg", "wb") as f:
    f.write(data)
```

## Position
```python
f.tell()                        # current byte offset
f.seek(offset, whence)          # 0=start (default), 1=current, 2=end
```
In text mode, only `seek(0)` and `seek(f.tell())` are portable — text offsets are opaque.

## Buffering and durability
Text files on a TTY are line-buffered; text files on disk are block-buffered. Data may live in Python or OS buffers until flushed:
```python
f.flush()                       # push Python buffers to the OS
os.fsync(f.fileno())            # force OS to write to disk
```
Closing a file (or leaving the `with` block) flushes but does not `fsync`.

## `pathlib`
`pathlib.Path` is the modern path API. `open()` accepts `Path` objects.
```python
from pathlib import Path

p = Path("data") / "input.txt"          # composition
p.exists(); p.stat().st_size
text  = p.read_text(encoding="utf-8")
data  = p.read_bytes()
p.write_text("hello\n", encoding="utf-8")
p.write_bytes(b"\x00\x01")

for csv in Path("data").glob("*.csv"):
    print(csv.name)
```
`read_text` / `write_text` open, read/write, and close in one call — convenient for small files.

## Atomic writes
`os.replace` is atomic on POSIX and Windows. Write to a sibling temp file, then rename:
```python
import os, tempfile
d = Path("data")
with tempfile.NamedTemporaryFile("w", dir=d, delete=False, encoding="utf-8") as tmp:
    tmp.write("new contents\n")
    tmp_path = tmp.name
os.replace(tmp_path, d / "out.txt")     # atomic swap
```
Prevents readers from seeing a half-written file.

## Standard serializers
```python
import json, csv

with open("config.json", encoding="utf-8") as f:
    cfg = json.load(f)

with open("data.csv", encoding="utf-8", newline="") as f:  # newline="" required
    for row in csv.reader(f):
        print(row)
```
`shutil` handles high-level copy/move; `tempfile` provides secure temp files and directories.

## Gotchas
- **`"w"` truncates immediately** — the moment `open` returns, the file is empty. Use `"a"` to preserve, `"x"` to fail-fast.
- **Default encoding varies** — always pass `encoding="utf-8"` for text. Do not rely on the platform default.
- **`write` doesn't add newlines** — include `\n` explicitly. Same for `writelines`.
- **Iterating a file is one-shot** — the position advances. Call `f.seek(0)` before iterating again.
- **CSV needs `newline=""`** — the `csv` module handles line endings itself; the default translation produces blank rows on Windows.
- **`with` matters** — a leaked file object may hold unflushed writes until it is garbage-collected.
- **`flush` is not `fsync`** — data can still be lost on power loss. Use `os.fsync` when durability matters.
