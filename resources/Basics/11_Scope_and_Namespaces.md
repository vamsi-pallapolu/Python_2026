# Scope & Namespaces

## What is scope?
**Scope** is where a variable is visible. When you use a name like `x`, Python searches for it in a fixed order — the **LEGB rule**: **L**ocal (this function) → **E**nclosing (outer function, if any) → **G**lobal (this file) → **B**uilt-in (Python's built-ins).

## LEGB — the lookup order
1. **Local** — names defined in the current function.
2. **Enclosing** — names in the local scope of any enclosing function (for nested functions).
3. **Global** — names at the top level of the current module.
4. **Built-in** — names in the `builtins` module (`len`, `range`, `print`, `Exception`, ...).

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)        # local

    inner()
    print(x)            # enclosing

outer()
print(x)                # global
```
Remove each `x = ...` line in turn to watch the lookup walk outward.

## `global` — assign to a module-level name
By default, assigning to `x` inside a function creates a **new local** `x`. To assign back to the module-level `x`, declare it `global`:
```python
count = 0

def bump():
    global count
    count += 1          # without `global`, this raises UnboundLocalError

bump()
count       # 1
```

## `nonlocal` — assign to an enclosing (non-global) name
Use inside a nested function to rebind a name in the nearest enclosing function scope.
```python
def make_counter():
    n = 0

    def bump():
        nonlocal n
        n += 1
        return n

    return bump

c = make_counter()
c()     # 1
c()     # 2
```
Without `nonlocal`, `n += 1` would try to read/write a *local* `n` and fail.

## Reading vs assigning
Python's scope rules are asymmetric:
- **Reading** a name walks LEGB.
- **Assigning** a name creates a **local** binding unless declared `global` or `nonlocal`.

```python
x = 10

def f():
    print(x)            # 10 — read walks up to global

def g():
    print(x)            # UnboundLocalError!
    x = 20              # this makes x local for the *entire* function
```
In `g`, Python sees the assignment `x = 20` and decides `x` is local — so the earlier `print(x)` fails before it ever runs.

## Namespaces at each level
| Namespace | Where it lives | Accessed via |
|-----------|---------------|--------------|
| Local | current function call | `locals()` |
| Enclosing | outer function's frame | (implicit — closure) |
| Global | current module | `globals()` |
| Built-in | `builtins` module | `import builtins` |

## Blocks that do **not** create a new scope
Unlike many languages, Python's `if`, `for`, `while`, `try`, and `with` blocks do **not** introduce a new scope. Names defined inside them leak into the surrounding function/module scope.
```python
for i in range(3):
    x = i
print(i, x)     # 2 2 — both are still visible
```
The exceptions that **do** create a new scope: **functions, classes, modules, and comprehensions** (`[e for e in ...]` has its own scope for the loop variable in Python 3+).

## Gotchas
- **Assignment anywhere in a function → local for the whole function.** Even if the first use is a read.
- **`global` inside a function only affects that function.** It doesn't create a global; it just tells this function "the `x` I'm using is the module-level one".
- **`nonlocal` requires an existing enclosing binding.** `nonlocal x` fails at compile time if no enclosing function defines `x`.
- **Loop variables leak** — after `for i in range(3):`, `i` is still `2` outside the loop.
- **Comprehensions have their own scope** — `[i for i in range(3)]` does **not** leak `i` (in Python 3+).
