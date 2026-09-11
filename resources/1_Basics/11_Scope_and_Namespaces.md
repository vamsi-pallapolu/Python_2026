# Scope and Namespaces

## Definition
A **name** is an identifier that refers to an object.

Variables are the most common kind of name, but function names, class names,
module names, and built-in names are names too.

```python
age = 25

def greet():
    print("Hello")

class Person:
    pass
```

In this example, `age`, `greet`, and `Person` are all names.

A **namespace** is a place where Python stores names and the objects they refer to.

A **scope** is the part of your program where a variable or other name can be used directly.

```python
username = "Vamsi"
print(username)
```

Here, `username` is a variable in the current namespace. Because `print(username)` is in the same scope, Python can find it.

## Name Lookup Order (LEGB)
When Python sees a name such as `x`, `print`, or `greet`, it searches in this order:

1. Local
2. Enclosing
3. Global
4. Built-in

This is called **LEGB**.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
```

Output:

```text
local
```

Python found the closest `x`, so it used `"local"`.

## Local Scope
Variables created inside a function usually belong only to that function.

```python
def greet():
    message = "Hello"
    print(message)

greet()
print(message)  # NameError
```

`message` exists only inside `greet`.

## Global Scope
A variable created outside any function is global to that file.

```python
count = 0

def show_count():
    print(count)

show_count()
```

Reading a global variable from inside a function is allowed.

## Assignment and Local Variables
If you assign to a variable inside a function, Python treats that variable as local.

```python
count = 0

def broken():
    count = count + 1
    print(count)

broken()
```

This raises `UnboundLocalError`.

Python thinks `count` is local because of `count = count + 1`, but the local `count` does not have a value yet.

## The `global` Keyword
Use `global` when a function needs to change a global variable.

```python
count = 0

def bump():
    global count
    count = count + 1

bump()
print(count)
```

Output:

```text
1
```

Use `global` carefully. In many programs, it is cleaner to return a new value instead.

```python
def bump(count):
    return count + 1

count = 0
count = bump(count)
```

## The `nonlocal` Keyword
Use `nonlocal` when an inner function needs to change a variable from an outer function.

```python
def make_counter():
    count = 0

    def bump():
        nonlocal count
        count = count + 1
        return count

    return bump

counter = make_counter()
print(counter())
print(counter())
```

Output:

```text
1
2
```

Without `nonlocal`, Python would create a new local `count` inside `bump`.

## Blocks and Scope
`if`, `for`, `while`, `try`, and `with` do not create a new scope.

```python
if True:
    result = "done"

print(result)
```

Output:

```text
done
```

The variable still exists after the `if` block.

## Function Scope
Functions create their own scope.

```python
def example():
    value = 10

example()
print(value)  # NameError
```

## Comprehension Scope
The loop variable inside a comprehension does not leak out.

```python
numbers = [1, 2, 3]
squares = [n * n for n in numbers]

print(squares)
print(n)  # NameError
```

## Common Mistakes
- Reading a variable before assigning it inside the same function.
- Using `global` when returning a value would be simpler.
- Expecting `if`, `for`, or `with` to hide variables. They do not.
- Expecting a method to access class variables by bare name.

```python
class Person:
    species = "human"

    def show_species(self):
        print(self.species)
```

Inside a method, use `self.species`, not just `species`.

## Summary
- A name is an identifier that refers to an object, such as a variable, function, class, module, or built-in.
- A namespace stores names and the objects they refer to.
- A scope decides where variables and other names can be used.
- Python searches names using LEGB: local, enclosing, global, built-in.
- Assigning to a variable inside a function makes it local unless you use `global` or `nonlocal`.
- Functions create scope; normal blocks like `if` and `for` do not.
