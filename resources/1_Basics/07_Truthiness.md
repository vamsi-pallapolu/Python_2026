# Truthiness

## Definition
Truthiness is how Python treats values as true or false in conditions.

```python
if value:
    print("truthy")
else:
    print("falsy")
```

Every value in Python is either truthy or falsy.

## Boolean Values
The two boolean values are:

```python
True
False
```

They are often returned by comparisons.

```python
print(10 > 5)
print(10 == 5)
```

Output:

```text
True
False
```

## Falsy Values
These common values are falsy:

| Value | Meaning |
|-------|---------|
| `False` | false boolean |
| `None` | no value |
| `0` | zero integer |
| `0.0` | zero float |
| `""` | empty string |
| `[]` | empty list |
| `()` | empty tuple |
| `{}` | empty dictionary |
| `set()` | empty set |

Example:

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")
```

## Truthy Values
Most other values are truthy.

```python
if "hello":
    print("non-empty strings are truthy")

if [0]:
    print("non-empty lists are truthy")
```

Important examples:

```python
bool("False")  # True
bool("0")      # True
bool([0])      # True
```

These are truthy because they are not empty.

## Using `bool()`
Use `bool()` to see the truth value of something.

```python
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("hello"))
```

Output:

```text
False
True
False
True
```

## `and`, `or`, and `not`
`and` is true only when both sides are truthy.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

`or` is true when at least one side is truthy.

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Can edit")
```

`not` reverses the truth value.

```python
logged_in = False

if not logged_in:
    print("Please log in")
```

## Default Values with `or`
`or` is often used to choose a default value.

```python
name = ""
display_name = name or "Guest"

print(display_name)
```

Output:

```text
Guest
```

This works because an empty string is falsy.

## Checking for `None`
Use `is None` when you specifically mean `None`.

```python
value = None

if value is None:
    print("missing")
```

Do not use `if not value` when `0`, `""`, or `[]` should be allowed values.

## `any()` and `all()`
`any()` returns `True` if at least one item is truthy.

```python
values = [0, "", "hello"]
print(any(values))
```

`all()` returns `True` if every item is truthy.

```python
values = [1, "yes", True]
print(all(values))
```

## Common Mistakes
- Thinking `"False"` is falsy. It is truthy because it is not empty.
- Thinking `"0"` is falsy. It is also truthy.
- Using `== True` instead of writing the condition directly.
- Using `if not value` when only `None` should count as missing.
- Forgetting that empty containers are falsy.

## Summary
- Truthiness decides how values behave in conditions.
- Empty values are usually falsy.
- Non-empty values are usually truthy.
- Use `is None` for checking `None`.
- Use `any()` and `all()` for groups of truth checks.
