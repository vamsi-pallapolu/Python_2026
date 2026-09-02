# Loops

Source: `src/1_Basics/7_loops.py`

## Definition
Loops repeat a block of code. Python has two main loop types:

- `for` loops for iterating over a sequence or iterable
- `while` loops for repeating while a condition is true

## `for` loop with `range()`
```python
n = 4

for i in range(0, n):
    print(i)
```

Output:
```text
0
1
2
3
```

`range(0, n)` starts at `0` and stops before `n`.

## Finding the minimum with a loop
```python
numbers = [10, 2, 3, 7]
minimum = numbers[0]

for value in numbers:
    if value <= minimum:
        minimum = value

print(f"Minimum:{minimum}")
```

Start with the first value, then compare every value against the current minimum.

Python also has a built-in:
```python
min(numbers)
```

Manual loops are useful for learning how the logic works.

## Iterating by index
```python
numbers = [10, 2, 3, 7]

for index in range(len(numbers)):
    print(index, numbers[index])
```

Use this when the index is needed. If only values are needed, iterate directly.

## `while` loop
```python
count = 0

while count < 3:
    count += 1
    print("Hello World")
```

A `while` loop needs:
- an initial value
- a condition
- an update that eventually makes the condition false

## Infinite loop
```python
while True:
    print("hello world")
```

This loop runs forever unless it reaches a `break`, raises an exception, or the program is stopped.

## Nested loops
Nested loops are loops inside loops.
```python
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()
```

Output:
```text
1
2 2
3 3 3
4 4 4 4
```

The outer loop controls the row. The inner loop controls how many values are printed in that row.

## Loop control
| Statement | Effect |
|-----------|--------|
| `break` | exit the nearest loop |
| `continue` | skip to the next iteration |
| `pass` | do nothing placeholder |

## Gotchas
- **`range(stop)` excludes `stop`**.
- **Avoid naming variables `min`** because it shadows the built-in `min()`.
- **A `while` loop must update its condition** or it may never stop.
- **Nested loops multiply work** - two loops can easily become O(n^2).
- **Use direct iteration when possible**: `for value in numbers`.
