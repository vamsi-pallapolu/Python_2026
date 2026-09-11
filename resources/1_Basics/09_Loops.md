# Loops

Source: `src/1_Basics/7_loops.py`

## Definition
Loops repeat a block of code.

Python has two main loop types:

- `for` loops
- `while` loops

## `for` Loops
Use a `for` loop to go through an iterable.

```python
names = ["Asha", "Ben", "Carlos"]

for name in names:
    print(name)
```

Output:

```text
Asha
Ben
Carlos
```

## `range()`
Use `range()` when you need a sequence of numbers.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

`range(5)` starts at `0` and stops before `5`.

Useful forms:

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 6)     # 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

## Looping by Index
Use indexes only when you need them.

```python
names = ["Asha", "Ben", "Carlos"]

for index in range(len(names)):
    print(index, names[index])
```

If you need both index and value, `enumerate()` is usually better.

```python
for index, name in enumerate(names):
    print(index, name)
```

## `while` Loops
Use a `while` loop when you want to repeat while a condition is true.

```python
count = 0

while count < 3:
    print("Hello")
    count = count + 1
```

A `while` loop usually needs:

- a starting value
- a condition
- an update

## Infinite Loops
An infinite loop keeps running until something stops it.

```python
while True:
    command = input("Command: ")

    if command == "quit":
        break
```

Use `break` to exit the loop.

## Loop Control Statements
| Statement | Meaning |
|-----------|---------|
| `break` | exit the nearest loop |
| `continue` | skip to the next iteration |
| `pass` | do nothing |

Example with `continue`:

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

## Nested Loops
A nested loop is a loop inside another loop.

```python
for row in range(3):
    for column in range(3):
        print(row, column)
```

Nested loops are useful for grids, tables, and combinations.

They can also become slow for large data, so use them carefully.

## Looping Through Dictionaries
Loop through keys:

```python
person = {"name": "Vamsi", "age": 25}

for key in person:
    print(key)
```

Loop through keys and values:

```python
for key, value in person.items():
    print(key, value)
```

## Common Mistakes
- Forgetting that `range(stop)` excludes `stop`.
- Creating an infinite `while` loop by forgetting to update the condition.
- Using indexes when direct iteration is clearer.
- Forgetting that `break` exits only the nearest loop.
- Making nested loops over large data without thinking about performance.

## Summary
- Use `for` to loop over iterables.
- Use `while` to loop while a condition is true.
- Use `range()` for number sequences.
- Use `break`, `continue`, and `pass` to control loops.
- Prefer direct iteration when possible.
