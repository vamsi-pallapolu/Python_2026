# Strings

Source: `DataStructures/1_string.py`

## What is a string?
A string is an **immutable sequence of Unicode characters**, used to store and manipulate text. Because strings are immutable, any operation that appears to modify a string (`replace`, concatenation, slicing) actually returns a **new string** object. Strings support indexing, slicing, iteration, and membership tests just like other sequences.

## Creation
```python
s1 = 'single'
s2 = "double"
s3 = """triple
        line"""
s4 = str(123)     # from another type
```

## Indexing
Strings are **sequences of characters** — accessed by 0-based index; negative indices count from the end.
```python
name = "Vamsi123@*()"
name[1]     # 'a'
name[-3]    # '*'
```
Out-of-range access raises `IndexError`.

## Slicing — `s[start:stop:step]`
- `stop` is exclusive.
- Any of the three parts can be omitted.
- A negative `step` reverses direction.
```python
s = "abcdef"
s[1:4]     # 'bcd'
s[:3]      # 'abc'
s[3:]      # 'def'
s[::-1]    # 'fedcba'   (reverse)
s[::2]     # 'ace'
```

## Iteration
```python
for ch in "ABCDEF":
    print(ch)
```

## Immutability
Strings **cannot be modified in place**. Any "update" creates a new object.
```python
s = "aBCD"
print(id(s))
s = 'A' + s[1:]
print(id(s))          # different id — new string
```

## Deletion
```python
s = 'vamsi'
del s          # deletes the name, not part of the string
```
You cannot delete a single character in place — build a new string with slicing.

## Updating a string
Since strings are immutable, "update" via slicing, concatenation, or `replace`:
```python
s  = "abcd"
s1 = "A" + s[1:]              # 'Abcd'
s2 = s.replace("abc", "AB1")  # 'AB1d'
```

## Concatenation and repetition
```python
"ab" + "cd"    # 'abcd'
"ab" * 3       # 'ababab'
```

## Membership
```python
"cat" in "concatenate"       # True
"z" not in "abc"             # True
```

## Common string methods
| Method | Purpose |
|--------|---------|
| `len(s)` | length |
| `s.lower()` / `s.upper()` | change case |
| `s.title()` / `s.capitalize()` / `s.swapcase()` | other case transforms |
| `s.strip()` / `s.lstrip()` / `s.rstrip()` | trim whitespace (or given chars) |
| `s.split(sep)` | split into a list |
| `sep.join(iterable)` | join iterable with `sep` |
| `s.replace(old, new)` | substitute all occurrences |
| `s.find(sub)` | first index, or `-1` if missing |
| `s.index(sub)` | first index, raises `ValueError` if missing |
| `s.startswith(p)` / `s.endswith(p)` | prefix / suffix check |
| `s.count(sub)` | number of non-overlapping occurrences |
| `s.isdigit()`, `s.isalpha()`, `s.isalnum()`, `s.isspace()` | classification |
| `s.zfill(n)` / `s.rjust(n, c)` / `s.ljust(n, c)` | padding |

## Escape sequences
| Sequence | Meaning |
|----------|---------|
| `\n`     | newline |
| `\t`     | tab |
| `\\`     | backslash |
| `\'` `\"` | quotes |
| `\uXXXX` | unicode codepoint |

## Raw strings
Prefix `r` — backslashes are treated literally (useful for regex and Windows paths).
```python
path = r"C:\new\test"           # no interpretation of \n, \t
regex = r"\d+\.\d+"
```

## Formatting (three ways)
```python
name, age = "Vamsi", 29
f"Hi {name}, age {age}"           # f-string  (preferred)
"Hi {}, age {}".format(name, age) # str.format
"Hi %s, age %d" % (name, age)     # old-style (C-like)
```

## Comparison
Compared lexicographically by Unicode code point.
```python
"apple" < "banana"       # True
"Z" < "a"                # True — uppercase comes before lowercase in ASCII
```
