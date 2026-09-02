# Scope & Namespaces

## Definition
A **namespace** is a mapping from names to objects. A **scope** is a textual region of code where a given namespace is directly accessible. Every module, function call, and class body has its own namespace; scope determines which namespaces Python searches when a bare name is used.

## LEGB lookup order
When a bare name is referenced, Python searches:

1. **L**ocal — the current function's local namespace.
2. **E**nclosing — the local namespace of each enclosing function, innermost first.
3. **G**lobal — the current module's top-level namespace.
4. **B**uilt-in — the `builtins` module (`len`, `range`, `print`, `Exception`, ...).

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)          # 'local'
    inner()
    print(x)              # 'enclosing'

outer()
print(x)                  # 'global'
```

Lookup stops at the first match. If no scope defines the name, `NameError`.

## Reading vs assigning
The rules are asymmetric:

- **Reading** a name walks LEGB at runtime.
- **Assigning** a name creates a binding in the **current scope** (local, for a function body) — unless declared `global` or `nonlocal`.

The classification is done at compile time by scanning the function body for assignments. Any assignment anywhere in the function marks the name local for the **entire** function, including reads that lexically precede it.

```python
x = 10
def g():
    print(x)              # UnboundLocalError
    x = 20                # this line makes x local everywhere in g
```

`del x` counts as an assignment for scope purposes — it produces the same classification.

## `global`
Declares that assignments to a name inside the function target the **module namespace**, not local.

```python
count = 0

def bump():
    global count
    count += 1            # without `global`, this raises UnboundLocalError
```

`global x` only affects the function it appears in; it does not create a global by itself.

## `nonlocal`
Declares that assignments target the **nearest enclosing function scope** (not module scope). The enclosing binding must already exist — the compiler rejects `nonlocal x` if no enclosing function defines `x`.

```python
def make_counter():
    n = 0
    def bump():
        nonlocal n
        n += 1
        return n
    return bump
```

Reading a captured name works without `nonlocal`; only rebinding requires it.

## `locals()` / `globals()` / `builtins`
- `locals()` — dict snapshot of the current local namespace. Writing to the returned dict does **not** update local variables in a function.
- `globals()` — the actual module namespace dict; mutating it does change module globals.
- `import builtins` — the built-in namespace, exposed as a module.

## `UnboundLocalError` vs `NameError`
- `NameError` — no scope in LEGB defines the name.
- `UnboundLocalError` — the name is classified local (some assignment in the function) but is read before that assignment executes.

## Class body scope
A class body is its own scope, but methods defined inside it do **not** see class-body names via enclosing lookup. Access class attributes through `cls.` (classmethod) or `self.` (instance method):

```python
class C:
    value = 1
    def get(self):
        return self.value          # not just `value`
```

Class-body names are visible during the body's execution (e.g. for decorators applied to methods) but are not part of the LEGB chain seen by nested functions.

## Comprehensions have their own scope
The loop variable and any names bound inside a comprehension live in an implicit function scope. They do not leak:

```python
[i for i in range(3)]
print(i)                  # NameError (in a fresh scope)
```

This also applies to generator, set, and dict comprehensions.

## Blocks that do **not** create a scope
`if`, `for`, `while`, `try`, and `with` do not introduce new scopes. Names bound inside them live in the enclosing function/module scope.

```python
for i in range(3):
    x = i
print(i, x)               # 2 2  — both survive
```

Scope-creating constructs: **modules, functions, class bodies, and comprehensions**.

## Gotchas
- **Any assignment makes a name local for the entire function.** Reads before the assignment raise `UnboundLocalError`.
- **`del x` counts as assignment** for scope classification. Deleting a name that would otherwise resolve globally makes it local instead.
- **`global` does not create a global** — it redirects assignments within one function to the module namespace. The name still needs to exist (or be assigned) at module level.
- **`nonlocal` requires an existing enclosing binding.** Fails at compile time otherwise.
- **Loop variables leak** — after `for i in range(3):`, `i == 2` in the enclosing scope. Comprehensions do not leak.
- **Writing to `locals()` in a function is not persistent** — it returns a snapshot dict; local variables live in a fixed-size frame array, not that dict.
