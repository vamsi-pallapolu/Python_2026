# Strings

Source: `DataStructures/1_string.py`

## Definition
A `str` is an **immutable sequence of Unicode code points**. Every operation that "changes" a string returns a new object.

## Creation
```python
s1 = 'single'
s2 = "double"
s3 = """triple
        line"""
s4 = str(123)          # from another type -> '123'
```
All four forms produce the same `str` type. Triple-quoted preserves embedded newlines.

## Indexing
Zero-based; negative indices count from the end. Out-of-range access raises `IndexError`.
```python
name = "Vamsi123"
name[1]      # 'a'
name[-1]     # '3'
```

## Slicing — `s[start:stop:step]`
`stop` is exclusive; any part may be omitted; negative `step` reverses direction. Slicing never raises — out-of-range bounds are clamped.
```python
s = "abcdef"
s[1:4]       # 'bcd'
s[:3]        # 'abc'
s[3:]        # 'def'
s[::-1]      # 'fedcba'
s[::2]       # 'ace'
```

## Immutability
No in-place edits — no item or slice assignment.
```python
s = "abc"
s[0] = 'A'          # TypeError
s = 'A' + s[1:]     # rebinding only; new object
```

## Concatenation, repetition, membership
```python
"ab" + "cd"          # 'abcd'
"ab" * 3             # 'ababab'
"cat" in "concat"    # True
```
Iteration yields code points one at a time:
```python
for ch in "abc":
    print(ch)
```

## Common methods
| Method | Purpose |
|--------|---------|
| `len(s)` | number of code points |
| `s.lower()` / `s.upper()` / `s.title()` / `s.capitalize()` | case transforms |
| `s.strip()` / `s.lstrip()` / `s.rstrip()` | trim whitespace (or given chars) |
| `s.split(sep)` / `s.rsplit(sep, n)` / `s.splitlines()` | split into list |
| `sep.join(iterable)` | join iterable of strings |
| `s.replace(old, new)` | substitute all occurrences |
| `s.find(sub)` / `s.rfind(sub)` | index or `-1` |
| `s.index(sub)` | index; raises `ValueError` |
| `s.startswith(p)` / `s.endswith(p)` | prefix / suffix — accept a tuple |
| `s.count(sub)` | non-overlapping occurrences |
| `s.isdigit()` / `.isalpha()` / `.isalnum()` / `.isspace()` | classification |
| `s.zfill(n)` / `s.ljust(n, c)` / `s.rjust(n, c)` | padding |
| `s.translate(t)` with `str.maketrans(src, dst)` | per-character mapping |

`split()` with no argument splits on runs of any whitespace and drops empty fields; `split(" ")` splits on single spaces and keeps empties.

## Escape sequences
| Sequence | Meaning |
|----------|---------|
| `\n` | newline |
| `\t` | tab |
| `\\` | backslash |
| `\'` `\"` | quotes |
| `\uXXXX` | unicode code point |

## Raw strings
Prefix `r` disables backslash interpretation — useful for regex and Windows paths.
```python
path  = r"C:\new\test"
regex = r"\d+\.\d+"
```

## Formatting
Three forms; **f-strings preferred**.
```python
name, age = "Vamsi", 29
f"Hi {name}, age {age}"             # f-string
"Hi {}, age {}".format(name, age)   # str.format (older)
"Hi %s, age %d" % (name, age)       # %-style (C-like, legacy)
```
F-string features:
```python
f"{value!r}"          # repr()
f"{value!s}"          # str()
f"{value!a}"          # ascii()
f"{x=}"               # debug: 'x=<value>'   (3.8+)
f"{n:>10}"            # right-align, width 10
f"{n:<10}"            # left-align
f"{pi:.2f}"           # 2 decimal places
f"{count:,}"          # thousands separator
f"{n:b}" / f"{n:o}" / f"{n:x}"   # binary / octal / hex
f"{x:e}"              # scientific
f"{ratio:%}"          # percent (multiplies by 100)
```

## Encoding
`str` is Unicode; bytes are a separate type. Convert with `encode`/`decode`; UTF-8 is the default.
```python
b = "café".encode("utf-8")     # b'caf\xc3\xa9'
b.decode("utf-8")              # 'café'
```

## Comparison
Lexicographic by Unicode code point.
```python
"apple" < "banana"     # True
"Z" < "a"              # True — 'Z'=0x5A, 'a'=0x61
```
`==` compares values; `is` compares identity. CPython interns some short/literal strings, so `is` may coincidentally return `True` — do not rely on it.

## Performance note
Concatenating in a loop is O(n^2) because each `+=` builds a new object:
```python
out = ""
for part in parts:
    out += part          # quadratic
out = "".join(parts)     # linear
```

## Gotchas
- **Immutable** — no in-place edits; slice-and-rebuild instead.
- **`find` vs `index`** — `find` returns `-1`, `index` raises `ValueError`.
- **`split()` vs `split(" ")`** — no-arg splits on any whitespace and drops empties; `split(" ")` does not.
- **`len(s)` counts code points, not bytes** — `len("café") == 4`, but its UTF-8 encoding is 5 bytes.
- **`is` for equality** — interning is an implementation detail. Use `==`.
- **Loop concatenation is quadratic** — use `"".join(parts)`.
