# Functions

Source: `src/1_Basics/8_functions.py`

## Definition
A function is a reusable block of code that runs when called.

```python
def evenOdd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")


evenOdd(10)
```

`def` defines the function. `evenOdd(10)` calls it.

## Parameters and arguments
Parameters are names in the function definition. Arguments are values passed during the function call.
```python
def evenOdd(x):      # x is a parameter
    ...

evenOdd(10)          # 10 is an argument
```

## Default arguments
Default arguments are used when the caller does not provide a value.
```python
def fun(arg1, arg2=40):
    print(arg1)
    print(arg2)


fun(10)
```

Here, `arg2` uses `40`.

## Keyword arguments
Keyword arguments pass values by parameter name, so order does not matter.
```python
def student(fname, lname):
    print(fname, lname)


student(fname="vamsi", lname="pallapolu")
student(lname="pallapolu", fname="vamsi")
```

## Arbitrary arguments
`*args` collects extra positional arguments into a tuple.

`**kwargs` collects extra keyword arguments into a dictionary.
```python
def myFun(*args, **kwargs):
    print("Extra Args")
    for arg in args:
        print(arg)

    print("Extra Keyword Args")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


myFun("hello", "world", fname="vamsi", lname="pallapolu")
```

## Pass by object reference
Python passes object references by assignment.

Mutable objects can be changed inside a function:
```python
def myFun(x):
    x[0] = 20


values = [10, 20, 30]
myFun(values)
print(values)             # [20, 20, 30]
```

Reassigning a local parameter does not reassign the caller's variable:
```python
def myFun(a):
    a = 20


a = 10
myFun(a)
print(a)                  # 10
```

## Assigning a function to a variable
Functions are objects, so they can be assigned to variables.
```python
x = 123


def show():
    x = 90
    print(x)
    print(globals()["x"])


f = show
f()
```

`globals()["x"]` accesses the global variable named `x`.

## Return values
The source examples print results, but functions can also return values.
```python
def is_even(x: int) -> bool:
    return x % 2 == 0
```

Use `return` when another part of the program needs the result.

## Gotchas
- **A function call needs parentheses** - `f` is the function object, `f()` calls it.
- **Mutable arguments can be changed inside a function**.
- **Reassigning a parameter only changes the local name**.
- **Default argument values are created once** - avoid mutable defaults like `[]`.
- **Use snake_case for function names** in normal Python style.
