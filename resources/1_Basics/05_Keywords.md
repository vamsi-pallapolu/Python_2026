# Keywords

Source: `src/1_Basics/4_keywords.py`

## Definition
Keywords are reserved words with special meaning in Python.

You cannot use keywords as variable names, function names, or class names.

```python
for = 10  # SyntaxError
```

## Viewing Keywords
Use the `keyword` module to see the keywords for your Python version.

```python
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
```

The list can change slightly between Python versions.

## Common Keyword Groups
| Group | Keywords |
|-------|----------|
| Conditions | `if`, `elif`, `else`, `match`, `case` |
| Loops | `for`, `while`, `break`, `continue` |
| Functions | `def`, `return`, `lambda` |
| Classes | `class` |
| Exceptions | `try`, `except`, `finally`, `raise` |
| Imports | `import`, `from`, `as` |
| Logic | `and`, `or`, `not`, `is`, `in` |
| Constants | `True`, `False`, `None` |
| Scope | `global`, `nonlocal` |
| Async | `async`, `await` |

## Soft Keywords
Some words are special only in certain syntax.

Example:

```python
match value:
    case 1:
        print("one")
```

`match` and `case` are soft keywords. They are special in pattern matching, but they can still be used as normal names in other places.

## Choosing Alternative Names
If the name you want is a keyword, choose a clearer name.

```python
for_count = 10
class_name = "Car"
value_type = "int"
```

Also avoid names that shadow common built-ins.

```python
list = [1, 2, 3]  # works, but not recommended
```

Use a better name:

```python
numbers = [1, 2, 3]
```

## Common Mistakes
- Using a keyword as a variable name.
- Forgetting that keywords are case-sensitive.
- Confusing `True` with `true`.
- Shadowing built-ins such as `list`, `str`, `min`, and `max`.
- Forgetting that soft keywords depend on context.

## Summary
- Keywords are reserved words in Python syntax.
- They cannot be used as normal identifiers.
- Use the `keyword` module to view them.
- Choose descriptive names that do not conflict with keywords or built-ins.
