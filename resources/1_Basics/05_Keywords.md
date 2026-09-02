# Keywords

Source: `src/1_Basics/4_keywords.py`

## Definition
Keywords are reserved words that have special meaning in Python syntax.

They cannot be used as variable names, function names, or class names.

```python
for = 10        # SyntaxError
```

## Viewing Python keywords
Use the `keyword` module to inspect the reserved words for the Python version you are running.
```python
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
```

The list can change slightly between Python versions.

## Common keyword groups
| Group | Keywords |
|-------|----------|
| Conditions | `if`, `elif`, `else`, `match`, `case` |
| Loops | `for`, `while`, `break`, `continue` |
| Functions | `def`, `return`, `lambda` |
| Classes | `class` |
| Exceptions | `try`, `except`, `else`, `finally`, `raise` |
| Imports | `import`, `from`, `as` |
| Boolean logic | `and`, `or`, `not`, `is`, `in` |
| Constants | `True`, `False`, `None` |
| Scope | `global`, `nonlocal` |
| Async | `async`, `await` |

## Soft keywords
Some words are only reserved in specific syntax contexts.

Examples in modern Python:
```python
match value:
    case 1:
        print("one")
```

`match` and `case` are soft keywords. They are special in pattern matching syntax but can still appear as ordinary names in other contexts.

## Valid alternatives
If a desired name is a keyword, choose a descriptive non-keyword name.
```python
for_count = 10
class_name = "Car"
value_type = "int"
```

## Gotchas
- **Keywords cannot be identifiers** - `for = 10` is invalid.
- **Python keywords are case-sensitive** - `True` is a keyword, `true` is not.
- **Avoid names that shadow built-ins** even if they are not keywords, such as `list`, `str`, `min`, and `max`.
- **Soft keywords depend on context** - they are not always fully reserved.
