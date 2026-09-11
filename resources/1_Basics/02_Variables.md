# Variables

Source: `src/1_Basics/2_variables.py`

## Definition
A variable is a name that refers to a value.

```python
name = "Vamsi"
age = 25
```

In Python, variables do not store the object directly. They refer to objects.

## Creating Variables
Use `=` to assign a value to a name.

```python
x = 10
message = "Hello"
is_active = True
```

Python decides the type from the value.

```python
print(type(x))
print(type(message))
```

## Naming Rules
Variable names:

- can contain letters, numbers, and underscores
- cannot start with a number
- cannot be Python keywords
- are case-sensitive

Valid names:

```python
age = 25
first_name = "Vamsi"
total_count = 10
```

Invalid names:

```python
2name = "bad"      # SyntaxError
class = "bad"      # SyntaxError
```

## Naming Style
Use `snake_case` for normal Python variables.

```python
first_name = "Vamsi"
total_price = 99.99
```

Avoid unclear names:

```python
x = 99.99
```

Use meaningful names:

```python
total_price = 99.99
```

## Assigning Multiple Variables
Assign the same value to several names:

```python
a = b = c = 20
```

Assign different values in one line:

```python
name, age, city = "Vamsi", 25, "New York"
```

The number of names must match the number of values.

## Rebinding Variables
You can point a variable name to a new value.

```python
x = 10
x = 20

print(x)
```

Output:

```text
20
```

This is called rebinding.

## Equality and Identity
Use `==` to compare values.

Use `is` to check whether two names refer to the exact same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
```

Output:

```text
True
False
True
```

Use `is` mainly for checks like:

```python
if value is None:
    print("missing")
```

## Deleting a Name
Use `del` to remove a name.

```python
x = 10
del x

print(x)  # NameError
```

`del` removes the name. It does not always destroy the object immediately.

## Swapping Values
Python can swap values directly.

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

Output:

```text
20 10
```

## Common Mistakes
- Using a Python keyword as a variable name.
- Using unclear names like `x` when a meaningful name would help.
- Confusing `=` with `==`.
- Using `is` when you mean value equality.
- Forgetting that assignment does not copy mutable objects.

## Summary
- A variable is a name that refers to a value.
- Use `=` for assignment.
- Use clear `snake_case` names.
- Use `==` for value comparison.
- Use `is None` for checking `None`.
