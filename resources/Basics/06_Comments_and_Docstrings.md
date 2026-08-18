# Comments & Docstrings

## What are comments and docstrings?
**Comments** are notes for humans — Python ignores them. **Docstrings** are short descriptions attached to a function, class, or file, so tools like `help()` and your IDE can show what it does. Rule of thumb: comments explain **why**, docstrings explain **what**.

## Single-line comments
Everything after `#` on a line is ignored.
```python
x = 10          # inline comment — explain the "why", not the "what"
# full-line comment
```

## Multi-line / block comments
Python has no block-comment syntax. Use consecutive `#` lines. A triple-quoted string sitting alone is technically a string literal, not a comment — the parser evaluates it and throws the result away.
```python
# For a longer note,
# use several # lines
# rather than triple quotes.
```

## Docstrings
The **first statement** in a module, function, class, or method — if it's a string literal — becomes that object's docstring.
```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

add.__doc__     # 'Return the sum of a and b.'
help(add)       # prints the signature + docstring
```

## Single-line vs multi-line docstrings
Follow **PEP 257**:
- One-liner: fits on a single line, ends with a period, summary in imperative mood.
- Multi-line: one-line summary → blank line → longer description → optional sections.

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

## Common docstring styles
Any consistent style is fine — pick one per project.

| Style | Looks like |
|-------|-----------|
| **Google** | `Args:`, `Returns:`, `Raises:` sections (shown above) |
| **NumPy** | `Parameters\n----------` underlined headings |
| **reST / Sphinx** | `:param x:`, `:returns:`, `:raises:` inline |

## When to use which
- Use a **docstring** on every public function, class, module, and method.
- Use a **comment** only when the code itself doesn't make the reason clear — a hidden constraint, a workaround, a non-obvious invariant.
- If the comment is describing *what* the code does, rename the variables/function instead.

## Gotchas
- **Triple-quoted strings are not comments** — they're evaluated (as expressions in most positions). Only in the docstring position are they attached to `__doc__`.
- **Docstring must be the very first statement** — not after `if TYPE_CHECKING:`, imports, or logic. Otherwise it's just a discarded string.
- **`#` inside a string is a literal `#`** — `"price: #1"` is fine; only `#` outside string literals begins a comment.
