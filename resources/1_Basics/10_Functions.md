# Functions

Source: `src/1_Basics/8_functions.py`

## Definition
A function is a reusable block of code.

Define a function with `def`.

```python
def greet():
    print("Hello")
```

Call a function with parentheses.

```python
greet()
```

## Parameters and Arguments
Parameters are names in the function definition.

Arguments are values passed to the function.

```python
def greet(name):
    print(f"Hello, {name}")

greet("Vamsi")
```

Here, `name` is a parameter and `"Vamsi"` is an argument.

## Return Values
Use `return` to send a result back to the caller.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

Output:

```text
5
```

If a function has no `return`, it returns `None`.

## Default Arguments
A default argument is used when the caller does not provide a value.

```python
def greet(name="friend"):
    print(f"Hello, {name}")

greet()
greet("Vamsi")
```

Output:

```text
Hello, friend
Hello, Vamsi
```

## Keyword Arguments
Keyword arguments pass values by parameter name.

```python
def student(first_name, last_name):
    print(first_name, last_name)

student(first_name="Vamsi", last_name="Pallapothu")
student(last_name="Pallapothu", first_name="Vamsi")
```

Keyword arguments make calls easier to read and allow flexible ordering.

## Positional Arguments
Positional arguments are matched by order.

```python
def divide(a, b):
    return a / b

print(divide(10, 2))
```

Here, `10` becomes `a` and `2` becomes `b`.

## `*args` and `**kwargs`
`*args` collects extra positional arguments into a tuple.

```python
def show_args(*args):
    print(args)

show_args(1, 2, 3)
```

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def show_kwargs(**kwargs):
    print(kwargs)

show_kwargs(name="Vamsi", age=25)
```

Advanced uses are covered in [13_Advanced_Functions.md](13_Advanced_Functions.md).

## Mutable Arguments
Python passes object references to functions.

If the object is mutable, the function can change it.

```python
def change_first(items):
    items[0] = "changed"

values = ["a", "b", "c"]
change_first(values)

print(values)
```

Output:

```text
['changed', 'b', 'c']
```

Reassigning the parameter itself does not reassign the caller's variable.

```python
def change_number(number):
    number = 99

x = 10
change_number(x)

print(x)
```

Output:

```text
10
```

## Functions as Objects
Functions are objects, so they can be assigned to variables.

```python
def say_hi():
    print("Hi")

func = say_hi
func()
```

`func` now refers to the same function as `say_hi`.

## Common Mistakes
- Forgetting parentheses when calling a function.
- Printing a value when the caller needs the function to return it.
- Using mutable default values such as `[]` or `{}`.
- Changing a mutable argument by accident.
- Using unclear function names.

## Summary
- Use `def` to define a function.
- Use parentheses to call a function.
- Parameters receive arguments.
- Use `return` to send back a result.
- Functions help organize and reuse code.
