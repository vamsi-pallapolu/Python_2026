# Functions

Source: `Basics/8_functions.py`

## What is a function?
A function is a **named, reusable block of code** that takes inputs (arguments), performs a task, and optionally returns a value. Functions promote code reuse, readability, and separation of concerns. In Python, functions are **first-class objects** — they can be assigned to variables, passed as arguments, and returned from other functions.

## Defining
```python
def evenOdd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

evenOdd(10)
```

## Default arguments
```python
def fun(arg1, arg2=40):
    print(arg1, arg2)

fun(10)          # arg2 defaults to 40
fun(10, 99)      # arg2 overridden
```

> **Pitfall — mutable defaults**: default values are evaluated **once** at definition time, so a mutable default is shared across all calls.
> ```python
> def bad(x, acc=[]):        # BUG: same list reused
>     acc.append(x); return acc
>
> def good(x, acc=None):
>     if acc is None: acc = []
>     acc.append(x); return acc
> ```

## Keyword arguments
Passing values by name — order doesn't matter.
```python
def student(fname, lname):
    print(fname, lname)

student(fname='vamsi', lname='pallapolu')
student(lname='pallapolu', fname='vamsi')
```

## Arbitrary arguments
- `*args`   — extra positional args collected as a **tuple**.
- `**kwargs`— extra keyword args collected as a **dict**.

```python
def myFun(*args, **kwargs):
    for a in args: print(a)
    for k, v in kwargs.items(): print(f"{k} = {v}")

myFun('hello', 'world', fname='vamsi', lname='pallapolu')
```

## Return values
- A function without an explicit `return` returns `None`.
- Multiple return values are returned as a tuple (which can be unpacked):
```python
def stats(xs):
    return min(xs), max(xs)

lo, hi = stats([3, 1, 2])
```

## Pass by object-reference
Python always passes **references** to objects. Whether the caller sees a mutation depends on **mutability**:

```python
def f(x): x[0] = 20                  # mutates the list — caller sees it
lst = [10, 20, 30]; f(lst)           # lst == [20, 20, 30]

def g(a): a = 20                     # rebinds local name only
a = 10; g(a)                         # a is still 10
```

## Scope (LEGB rule)
Python resolves names in this order:
1. **L**ocal — inside the current function.
2. **E**nclosing — outer functions (closures).
3. **G**lobal — module-level.
4. **B**uilt-in — `len`, `print`, `sum`, ...

```python
x = 123
def show():
    x = 90                    # local x
    print(x)                  # 90
    print(globals()['x'])     # 123
```

- `global x`   — assignments inside the function target the **module-level** name.
- `nonlocal x` — assignments target the nearest **enclosing** (non-global) scope.

## Functions are first-class objects
They can be assigned to variables, passed as arguments, returned, and stored in containers.
```python
def show(): print("hi")
f = show                # bind another name
f()                     # call via new name
```

## Lambdas — anonymous functions
Single-expression functions, typically used inline.
```python
square = lambda x: x * x
items_sorted = sorted(people, key=lambda p: p.age)
```

## Docstrings
The first string literal in a function is its documentation.
```python
def area(r):
    """Return the area of a circle with radius r."""
    return 3.14159 * r * r

help(area)
```

## Type hints (optional, since 3.5)
Hints don't enforce types at runtime — they're used by editors and type checkers.
```python
def add(a: int, b: int) -> int:
    return a + b
```
