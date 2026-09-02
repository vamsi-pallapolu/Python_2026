# Input / Output

Source: `Basics/1_io.py`

## Definition
Input/Output is the transfer of data between a program and its environment. Python exposes it through built-ins that operate on text streams — `input()` reads a line from `sys.stdin`, `print()` writes to `sys.stdout`. Both operate on `str`; conversion between text and other types is explicit.

## `print()`
Signature: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`. Each object is converted via `str()`, joined by `sep`, followed by `end`, and written to `file`.
```python
print("a", "b", "c")               # a b c
print("a", "b", sep="-")           # a-b
print("no newline", end="")
print("error!", file=sys.stderr)
```

`flush=True` forces the stream buffer out immediately — required when stdout is line-buffered in a terminal but block-buffered in a pipe or file (progress bars, live logs).
```python
for i in range(3):
    print(".", end="", flush=True)
```

## `input()`
Reads until newline, strips the trailing `\n`, returns a `str`. Blocks until Enter is pressed. Raises `EOFError` on end-of-stream.
```python
name = input("Name: ")             # always str
age  = int(input("Age: "))         # convert explicitly
pi   = float(input("π? "))
```

## Reading multiple values
`str.split()` on whitespace produces a list of tokens; `map` applies a conversion lazily.
```python
x, y = input().split()             # both str
a, b = map(int, input().split())   # both int
nums = list(map(float, input().split()))
```

## f-strings
Formatted string literals. Expressions inside `{...}` are evaluated at runtime; the result is formatted per the optional format spec.
```python
name, n = "Ann", 3.14159
f"{name}"                          # 'Ann'
f"{1 + 2}"                         # '3'
f"{n:.2f}"                         # '3.14'
```

### Conversion flags
`!r` calls `repr()`, `!s` calls `str()` (default), `!a` calls `ascii()`. Use `!r` to render quoted, unambiguous debug output.
```python
s = "hi\n"
f"{s!s}"                           # 'hi\n' (as text)
f"{s!r}"                           # "'hi\\n'"
```

### Debug form
`{expr=}` emits both the source text and its value — handy in log lines without repeating the name.
```python
x = 42
f"{x=}"                            # 'x=42'
f"{x*2=}"                          # 'x*2=84'
```

### Format spec
Syntax: `[[fill]align][sign][#][0][width][,][.precision][type]`.
```python
f"{'hi':>10}"                      # '        hi'   right-align, width 10
f"{'hi':<10}"                      # 'hi        '
f"{'hi':^10}"                      # '    hi    '
f"{1234567:,}"                     # '1,234,567'
f"{0.5:.2%}"                       # '50.00%'
f"{255:b}"                         # '11111111'
f"{255:o}"                         # '377'
f"{255:x}"                         # 'ff'
f"{255:#x}"                        # '0xff'
```

## Older formatting
Still valid; f-strings supersede them.
```python
"Hello, {}".format(name)           # str.format — positional / named fields
"Hello, %s" % name                 # % — C-style, kept for legacy code
```

## How output is buffered
`sys.stdout` is line-buffered when connected to a TTY (flushes on `\n`) and block-buffered when redirected to a pipe or file. `print(..., flush=True)` or `sys.stdout.flush()` forces a write regardless.

## Gotchas
- **`input()` always returns `str`** — arithmetic on it silently concatenates or raises `TypeError`. Convert explicitly.
- **`int(input())` on non-numeric input raises `ValueError`** — wrap in `try/except` for user-facing prompts.
- **Progress output disappears under a pipe** — buffering is block-based, not line-based. Pass `flush=True`.
- **Non-ASCII output on Windows consoles** — depends on the active code page; set `PYTHONIOENCODING=utf-8` or use `sys.stdout.reconfigure(encoding='utf-8')`.
- **`print(a, b)` inserts a space by default** — pass `sep=""` to concatenate.
- **`input()` does not evaluate its argument as a prompt** — it prints it via `sys.stdout` first. If stdout is redirected, the prompt goes with it, not to the terminal.
