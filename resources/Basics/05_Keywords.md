# Keywords

Source: `Basics/4_keywords.py`

## Definition
Keywords are reserved identifiers with a fixed grammatical role. The parser recognizes them as syntax tokens, so they cannot be bound as names (variables, function names, parameters, attributes via `setattr` still work). Python splits them into **hard** keywords (always reserved) and **soft** keywords (reserved only in specific grammar positions).

```python
# for = 10          # SyntaxError — 'for' is a hard keyword
```

## Hard keywords
Always reserved; listed in `keyword.kwlist`.

```
False    None     True     and      as       assert   async    await
break    class    continue def      del      elif     else     except
finally  for      from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise    return   try
while    with     yield
```

## Soft keywords
Reserved only in the positions the grammar expects them; usable as normal identifiers elsewhere. Listed in `keyword.softkwlist`.

```
match    case    type    _
```

```python
match = 5                    # legal — 'match' is only reserved before a subject
case = "ok"                  # legal — not at the start of a case clause
type = int                   # legal, but shadows the builtin
```

`keyword.iskeyword("match")` returns `False`; use `keyword.issoftkeyword("match")` to detect soft keywords.

## Grouped by purpose
| Group        | Keywords |
|--------------|----------|
| Values       | `True`, `False`, `None` |
| Logical ops  | `and`, `or`, `not` |
| Conditionals | `if`, `elif`, `else`, `match`, `case` |
| Loops        | `for`, `while`, `break`, `continue`, `else` |
| Functions    | `def`, `return`, `lambda`, `yield` |
| Classes/OOP  | `class` |
| Imports      | `import`, `from`, `as` |
| Exceptions   | `try`, `except`, `finally`, `raise`, `assert` |
| Scope        | `global`, `nonlocal` |
| Context/async| `with`, `async`, `await` |
| Identity/membership | `is`, `in` |
| Misc         | `pass`, `del`, `type` |

`self` and `super` are not keywords — `self` is a convention, `super` is a builtin function.

## `async` / `await`
Introduced in 3.5 as context-dependent tokens, promoted to full reserved keywords in 3.7. `async def` marks a coroutine; `await` suspends until an awaitable resolves and is only valid inside `async` functions.

```python
async def fetch(url):
    data = await client.get(url)
    return data
```

## `pass` vs `...` (Ellipsis)
Both act as no-op placeholders in a body, but they are different constructs.

```python
def not_yet():
    pass                     # statement — does nothing

def stub() -> int:
    ...                      # expression — the Ellipsis singleton
```

- `pass` is a statement; the only thing it does is satisfy the grammar's need for a body.
- `...` is the `Ellipsis` object. It also appears in type stubs (`.pyi` files), abstract method bodies, and slice syntax for NumPy (`arr[..., 0]`).

## Runtime checks with the `keyword` module
```python
import keyword

keyword.kwlist              # list of hard keywords
keyword.softkwlist          # ['_', 'case', 'match', 'type']
keyword.iskeyword("for")    # True
keyword.iskeyword("match")  # False — soft keyword
keyword.issoftkeyword("match")  # True
```

## Gotchas
- **Cannot rebind hard keywords** — `True = 0` and `def = 1` are syntax errors.
- **Soft keywords shadow builtins** — `type = int` is legal but breaks `type(x)` for the rest of the scope. Same risk with `match` shadowing `re.match` after `from re import match`.
- **Trailing-underscore convention** — when you need a name that collides with a keyword, use `class_`, `type_`, `from_`. Common in libraries that wrap SQL or HTTP.
- **`_` is a soft keyword** — reserved only as the wildcard pattern inside `case`. Everywhere else it is a normal identifier and a REPL convention for the last result.
