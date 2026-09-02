# Basics — Roadmap

Mandatory Python basics to cover before moving on to advanced topics (OOP, decorators, concurrency, stdlib deep-dives, etc.). Ordered by dependency — earlier items unlock later ones. Numbering matches `resources/Basics/`.

Legend: `[x]` covered · `[ ]` pending

## 1. Language mechanics (00–05)
- [x] 00 — About Python
- [x] 01 — Input / Output — `input()`, `print()`, f-strings
- [x] 02 — Variables & assignment
- [x] 03 — Data types — `int`, `float`, `str`, `bool`, `None`, `list`, `tuple`, `dict`, `set`
- [x] 04 — Operators — arithmetic, comparison, logical, bitwise, identity, membership
- [x] 05 — Keywords & reserved names

## 2. Control flow (06–09)
- [x] 06 — Comments & docstrings — `#`, `"""..."""`, PEP 257 conventions
- [x] 07 — Truthiness — falsy values (`0`, `""`, `[]`, `None`, `{}`), short-circuit `and`/`or`
- [x] 08 — Conditional statements — `if / elif / else`
- [x] 09 — Loops — `for`, `while`, `break`, `continue`, `else` on loops

## 3. Functions (10–13)
- [x] 10 — Function basics — `def`, parameters, return values, positional vs keyword args
- [x] 11 — Scope & namespaces — LEGB rule, `global`, `nonlocal`
- [x] 12 — Type hints / annotations — `x: int`, `def f(a: str) -> bool:`, `list[int]`, `Optional`
- [x] 13 — Advanced functions — `*args`/`**kwargs`, default-arg trap, `lambda`, first-class functions, closures

## 4. Errors & resource management (14–15)
- [x] 14 — Exceptions — `try / except / else / finally`, `raise`, chaining with `from`, custom exceptions
- [x] 15 — Context managers — `with` statement, resource cleanup, files, locks

## 5. Iteration primitives (16–17)
- [x] 16 — Iteration helpers — `range`, `enumerate`, `zip`
- [x] 17 — Generators — `yield`, generator expressions vs list comprehensions, `iter()` / `next()`

## 6. Modules & I/O (18–20)
- [x] 18 — Modules & imports — `import`, `from ... import`, aliasing, packages, `if __name__ == "__main__":`
- [x] 19 — File I/O — `open()`, read/write modes (`r`/`w`/`a`/`rb`/`wb`), `with open(...) as f:`
- [x] 20 — Virtual environments & `pip` — `venv`, `requirements.txt`, installing packages
