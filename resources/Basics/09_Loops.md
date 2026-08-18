# Loops

Source: `Basics/7_loops.py`

## What is a loop?
A loop **runs the same block of code multiple times**. Python has two kinds: `for` (loop over items in a list, string, or range) and `while` (loop while a condition is true).

## `for` loop
Iterates over any iterable (list, tuple, string, range, dict, generator, ...).
```python
for i in range(0, n):        # 0, 1, ..., n-1
    print(i)

for x in [10, 2, 3, 7]:      # iterate items directly
    ...

for i, x in enumerate(nums): # index + value
    ...

for k, v in {"a": 1}.items():
    ...
```

## `while` loop
```python
count = 0
while count < 3:
    count += 1
    print("Hello World")
```

Infinite loop — needs a `break` to exit:
```python
while True:
    line = input()
    if line == "quit":
        break
```

## Loop control
- `break` — exit the nearest enclosing loop.
- `continue` — skip to the next iteration.
- `else` on a loop — runs **only if** the loop finished without hitting `break`.

```python
for x in nums:
    if x == target:
        print("found")
        break
else:
    print("not found")
```

## Nested loops
```python
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
# Output (each row has a trailing space from end=' '):
# 1
# 2 2
# 3 3 3
# 4 4 4 4
```

## `range()`
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

`stop` is **exclusive**. `step` can be negative:
```python
list(range(5, 0, -1))     # [5, 4, 3, 2, 1]
```

## Comprehensions (loop as an expression)
```python
squares = [x*x for x in range(10)]
evens   = [x for x in nums if x % 2 == 0]
lookup  = {name: len(name) for name in names}
uniq    = {c.lower() for c in text}
```
