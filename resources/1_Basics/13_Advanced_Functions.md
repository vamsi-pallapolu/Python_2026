# Advanced Functions

## Definition
Python functions can do more than take a few arguments and return a value.

In Python, functions are also objects. You can:

- pass a function into another function
- return a function from another function
- store functions in variables
- wrap one function with another function

This file covers the most common patterns.

## Variable-Length Positional Arguments (`*args`)
Use `*args` when a function can accept any number of positional arguments.

Inside the function, `args` is a tuple.

```python
def show_items(*args):
    print(args)

show_items("apple", "banana", "orange")
```

Output:

```text
('apple', 'banana', 'orange')
```

You can loop over `args`.

```python
def total(*numbers):
    result = 0

    for number in numbers:
        result = result + number

    return result

print(total(1, 2, 3))
print(total(10, 20, 30, 40))
```

Output:

```text
6
100
```

## Variable-Length Keyword Arguments (`**kwargs`)
Use `**kwargs` when a function can accept any number of keyword arguments.

Inside the function, `kwargs` is a dictionary.

```python
def show_profile(**kwargs):
    print(kwargs)

show_profile(name="Vamsi", age=25, city="New York")
```

Output:

```text
{'name': 'Vamsi', 'age': 25, 'city': 'New York'}
```

You can loop through the dictionary.

```python
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_profile(name="Vamsi", age=25)
```

## Combining `*args` and `**kwargs`
`*args` comes before `**kwargs`.

```python
def show_all(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show_all(1, 2, 3, name="Vamsi", active=True)
```

Output:

```text
args: (1, 2, 3)
kwargs: {'name': 'Vamsi', 'active': True}
```

This is useful when one function passes arguments to another function.

```python
def add(a, b):
    return a + b

def wrapper(*args, **kwargs):
    print("Before call")
    result = add(*args, **kwargs)
    print("After call")
    return result

print(wrapper(2, 3))
```

## Argument Unpacking
At the call site, `*` unpacks a list or tuple into positional arguments.

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))
```

Output:

```text
6
```

`**` unpacks a dictionary into keyword arguments.

```python
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}"

person = {"first_name": "Vamsi", "last_name": "Pallapothu"}
print(greet(**person))
```

## Keyword-Only Arguments
Sometimes you want an argument to be passed by name.

Use `*` before it.

```python
def create_user(name, *, is_admin=False):
    print(name, is_admin)

create_user("Vamsi", is_admin=True)
```

This call is not allowed:

```python
create_user("Vamsi", True)  # TypeError
```

Keyword-only arguments make calls clearer when a value could be confusing.

## Mutable Default Values
Be careful with default values like lists and dictionaries.

Default values are created once when Python defines the function, not every time the function runs.

```python
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad("a"))
print(add_item_bad("b"))
```

Output:

```text
['a']
['a', 'b']
```

Both calls used the same list.

Use `None` instead.

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))
```

Output:

```text
['a']
['b']
```

## Lambda Functions
A `lambda` is a small function written in one line.

```python
square = lambda number: number * number

print(square(5))
```

Output:

```text
25
```

Lambdas are most useful when passed directly into another function.

```python
words = ["banana", "fig", "apple"]

print(sorted(words, key=lambda word: len(word)))
```

Output:

```text
['fig', 'apple', 'banana']
```

If the function needs more than one simple expression, use `def`.

```python
def square(number):
    return number * number
```

## Functions as Values
Functions can be stored in variables.

```python
def shout(text):
    return text.upper()

make_loud = shout

print(make_loud("hello"))
```

Output:

```text
HELLO
```

Functions can also be passed into other functions.

```python
def apply(func, value):
    return func(value)

print(apply(shout, "hello"))
```

## Returning Functions
A function can create and return another function.

```python
def make_multiplier(amount):
    def multiply(number):
        return number * amount

    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))
print(triple(10))
```

Output:

```text
20
30
```

The inner function remembers `amount`. This is called a **closure**.

## Closures and `nonlocal`
If an inner function needs to change a variable from the outer function, use `nonlocal`.

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

See [11_Scope_and_Namespaces.md](11_Scope_and_Namespaces.md) for more scope rules.

## Decorators
A decorator wraps a function with another function.

```python
def trace(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

@trace
def say_hello():
    print("Hello")

say_hello()
```

Output:

```text
Before
Hello
After
```

This:

```python
@trace
def say_hello():
    print("Hello")
```

means this:

```python
def say_hello():
    print("Hello")

say_hello = trace(say_hello)
```

## Decorators with Arguments
Use `*args` and `**kwargs` inside a decorator wrapper when the wrapped function may receive arguments.

```python
def trace(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)

    return wrapper

@trace
def add(a, b):
    return a + b

print(add(2, 3))
```

Output:

```text
Calling function
5
```

## Preserving Metadata with `functools.wraps`
When writing decorators, use `functools.wraps`.

It keeps the original function name and documentation.

```python
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)

    return wrapper
```

This helps debugging and editor tools.

## Partial Functions
`partial` creates a new function with some arguments already filled in.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))
print(cube(5))
```

Output:

```text
25
125
```

## Caching with `functools.cache`
`cache` remembers previous results.

This is useful when a function is expensive and may receive the same arguments again.

```python
from functools import cache

@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
```

Output:

```text
55
```

Function arguments must be hashable to be cached. Simple values like strings, integers, and tuples are usually fine.

## Callable Objects
An object can act like a function if it has a `__call__` method.

```python
class Adder:
    def __init__(self, amount):
        self.amount = amount

    def __call__(self, number):
        return number + self.amount

add_five = Adder(5)

print(add_five(10))
print(callable(add_five))
```

Output:

```text
15
True
```

## Common Mistakes
- Putting `**kwargs` before `*args`. Use `*args` first.
- Using a mutable default value like `[]` or `{}`.
- Using `lambda` when a normal `def` would be easier to read.
- Forgetting `nonlocal` when changing a captured variable.
- Writing a decorator wrapper that cannot accept the original function's arguments.
- Forgetting `functools.wraps` in decorators.

## Summary
- `*args` collects extra positional arguments.
- `**kwargs` collects extra keyword arguments.
- `*` and `**` can also unpack arguments when calling a function.
- Functions can be stored, passed, and returned.
- A closure is an inner function that remembers values from an outer function.
- A decorator wraps one function with another function.
