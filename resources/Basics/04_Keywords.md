# Keywords

Source: `Basics/4_keywords.py`

## What is a keyword?
A keyword is a **reserved word** built into the language that has a fixed meaning and defines the grammar of Python (e.g. `if`, `for`, `def`, `class`, `return`). They cannot be used as identifiers — you can't name a variable, function, or class after a keyword. Python 3.10+ also has *soft* keywords (`match`, `case`) which are reserved only in context.

```python
# for = 10        # SyntaxError — 'for' is a keyword
```

## Complete list (Python 3.10+)
```
False    None     True     and      as       assert   async    await
break    class    continue def      del      elif     else     except
finally  for      from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise    return   try
while    with     yield    match    case
```
> `match` / `case` are **soft** keywords (reserved only in that context).

## Check keywords at runtime
```python
import keyword
print(keyword.kwlist)          # list of all keywords
keyword.iskeyword("for")       # True
keyword.iskeyword("foo")       # False
```

## Grouped by purpose
| Group        | Keywords |
|--------------|----------|
| Values       | `True`, `False`, `None` |
| Logical ops  | `and`, `or`, `not` |
| Conditionals | `if`, `elif`, `else`, `match`, `case` |
| Loops        | `for`, `while`, `break`, `continue`, `else` |
| Functions    | `def`, `return`, `lambda`, `yield` |
| Classes/OOP  | `class`, `self` (convention, not keyword), `super` (builtin) |
| Imports      | `import`, `from`, `as` |
| Exceptions   | `try`, `except`, `finally`, `raise`, `assert` |
| Scope        | `global`, `nonlocal` |
| Misc         | `pass`, `del`, `in`, `is`, `with`, `async`, `await` |
