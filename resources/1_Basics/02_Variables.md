# Variables

Source: `src/1_Basics/2_variables.py`

## Definition
A variable is a name that refers to an object. Python variables store references to objects, not the actual object data directly.

```python
x = 1
y = x
```

Both names can refer to the same object until one name is rebound.

## Assigning the same value to multiple variables
```python
a = b = c = 20
print(a, b, c)
```

All three names refer to the same integer object `20`.

## Assigning different values in one line
```python
x, y, z = "vamsi", 29, "mathworks"
print(x, y, z)
```

This is called unpacking assignment. The number of names must match the number of values.

## Rebinding a variable
```python
x = 1
y = x
y = y + 1

print(x)     # 1
print(y)     # 2
```

`y = y + 1` does not change `x`. It creates or finds a new value and rebinds `y`.

## Deleting a variable
```python
z = 30
del z
```

After `del z`, the name `z` is removed. Using it again raises `NameError`.

## Object identity
`id()` returns an object's identity during its lifetime.
```python
v1 = [1, 2, 3]
v2 = [1, 2, 3]

print(id(v1))
print(id(v2))
```

Even though the lists have equal values, they are two different objects.

```python
v1 == v2      # True: same contents
v1 is v2      # False: different objects
```

## Swapping variables
Python supports clean variable swapping.
```python
a, b = 10, 20
a, b = b, a
```

No temporary variable is needed.

## Practical example: string length
```python
word = "Python"
length = len(word)
print("Length of word", length)
```

`len()` returns the number of characters in the string.

## Gotchas
- **Assignment binds names to objects** - it does not copy objects by default.
- **`==` checks value equality**; **`is` checks identity**.
- **`del` removes a name**, not necessarily the object immediately.
- **Unpacking counts must match** - `x, y = 1, 2, 3` raises `ValueError`.
- **Avoid shadowing built-ins** like `list`, `min`, `max`, and `str`.
