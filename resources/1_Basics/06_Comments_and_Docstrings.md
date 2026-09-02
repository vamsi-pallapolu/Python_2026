# Comments & Docstrings

## Definition
A **comment** is source text the tokenizer discards — it has no runtime effect. A **docstring** is a real string literal that the compiler attaches to a module, class, or function object as `__doc__` when it appears as the first statement of that body. Comments explain *why*; docstrings document *what* and are queryable at runtime.

## Line comments
Everything from `#` to end-of-line is stripped by the tokenizer. Python has no block-comment syntax.

```python
x = 10          # inline comment
# full-line comment
```

For a multi-line note use consecutive `#` lines. A triple-quoted string on its own is a string *expression* whose result is discarded — legal, but it is not a comment and the parser still evaluates it.

```python
# For a longer note, use
# several # lines rather than
# a triple-quoted string.
```

## Docstrings
The **first statement** of a module, class, function, or method — if it is a string literal — is bound to that object's `__doc__` attribute. Anything later, even another string literal, is not a docstring.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

add.__doc__          # 'Return the sum of a and b.'
help(add)            # prints signature + docstring via pydoc
```

## PEP 257 conventions
- One-liner: fits one line, imperative mood, ends with a period.
- Multi-line: summary line → blank line → body → optional sections. Closing `"""` on its own line.

```python
def fetch_user(user_id):
    """Fetch a user by ID from the primary database.

    Args:
        user_id: The user's integer ID.

    Returns:
        A User instance, or None if not found.

    Raises:
        DatabaseError: If the connection fails.
    """
    ...
```

## Docstring styles
Sphinx, IDEs, and doc generators parse these. Pick one per project.

| Style | Section markers |
|-------|-----------------|
| Google | `Args:`, `Returns:`, `Raises:` |
| NumPy  | `Parameters` / `Returns` under `----------` |
| reST   | `:param x:`, `:returns:`, `:raises:` |

## `help()` and `pydoc`
`help(obj)` walks the MRO and prints the object's signature plus `__doc__`. `pydoc` (CLI: `python -m pydoc name`) uses the same machinery to render HTML or terminal docs.

## `doctest` — executable examples
The `doctest` module scans docstrings for interactive-session lines (`>>>`) and runs them as tests.

```python
def add(a, b):
    """Return the sum.

    >>> add(2, 3)
    5
    """
    return a + b

# python -m doctest module.py -v
```

## Directive-style comments
Some `#`-comments are read by external tools even though Python ignores them.

```python
#!/usr/bin/env python3       # shebang — the OS uses this to pick the interpreter
# -*- coding: utf-8 -*-      # PEP 263 source encoding (default is utf-8 since 3.0)
x: int = "oops"  # type: ignore   # silence a type checker on this line
import os  # noqa: F401           # tell flake8/ruff to skip a rule
# fmt: off                        # black/ruff-format: preserve manual formatting
# fmt: on
```

## `from __future__ import annotations`
Not a comment, but a directive-shaped statement: it changes how the compiler treats annotations (they become strings, evaluated lazily). Must appear before any non-docstring code.

```python
from __future__ import annotations

def head(xs: list[int]) -> int:   # 'list[int]' stored as a string, not evaluated
    return xs[0]
```

## Gotchas
- **Docstring must be the first statement** — placing it after imports, `if TYPE_CHECKING:`, or logic makes it a discarded expression, not `__doc__`.
- **Triple-quoted strings are not comments** — they are string literals. In an expression position they build a `str` object; only in the docstring position are they attached to `__doc__`.
- **`#` inside a string literal is not a comment** — `"price: #1"` is a plain string. Comments are recognized by the tokenizer only outside strings.
- **Explain *why*, not *what*** — if a comment paraphrases the code, rename the variable or extract a function instead. Reserve comments for constraints, invariants, workarounds, and links to issues.
- **Docstrings survive `python -O`; `assert` does not** — never rely on `assert` for runtime checks that must stick, but docstring-based tools keep working.
