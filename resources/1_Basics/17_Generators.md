# Generators

## Definition
A generator creates values one at a time.

This is useful when:

- there are many values
- you do not need all values at once
- you want to write a simple loop that produces data

## Generator Functions
A generator function uses `yield`.

```python
def count_to_three():
    yield 1
    yield 2
    yield 3
```

Calling the function does not run the body immediately.

```python
numbers = count_to_three()
print(numbers)
```

It creates a generator object.

To get values, loop over it:

```python
for number in count_to_three():
    print(number)
```

Output:

```text
1
2
3
```

## How `yield` Works
When Python reaches `yield`, it gives a value back and pauses the function.

The next time you ask for a value, the function continues after the `yield`.

```python
def count_up_to(limit):
    number = 1

    while number <= limit:
        yield number
        number = number + 1

counter = count_up_to(3)

print(next(counter))
print(next(counter))
print(next(counter))
```

Output:

```text
1
2
3
```

After the generator is finished, another `next(counter)` raises `StopIteration`.

## One-Time Iteration
Once a generator is used up, it is empty.

```python
numbers = count_up_to(3)

print(list(numbers))
print(list(numbers))
```

Output:

```text
[1, 2, 3]
[]
```

Create a new generator if you need to loop again.

```python
print(list(count_up_to(3)))
print(list(count_up_to(3)))
```

## Generator Expressions
A generator expression looks like a list comprehension, but uses parentheses.

```python
squares = (number * number for number in range(5))
```

It does not build a full list.

```python
print(sum(number * number for number in range(5)))
```

Output:

```text
30
```

Compare:

```python
squares_list = [number * number for number in range(5)]
squares_generator = (number * number for number in range(5))
```

The list stores all results.

The generator produces results one at a time.

## Why Use Generators?
Generators can save memory.

```python
def read_lines(path):
    with open(path) as file:
        for line in file:
            yield line.strip()
```

This reads one line at a time instead of loading the whole file into memory.

You can use it like this:

```python
for line in read_lines("data.txt"):
    print(line)
```

## The `yield from` Statement
Use `yield from` to yield all values from another iterable.

```python
def numbers():
    yield 1
    yield 2

def more_numbers():
    yield 0
    yield from numbers()
    yield 3

print(list(more_numbers()))
```

Output:

```text
[0, 1, 2, 3]
```

This is simpler than writing another loop:

```python
for number in numbers():
    yield number
```

## Generators vs Lists
Use a list when you need to:

- keep all values
- check the length
- use indexing
- loop more than once

Use a generator when you want to:

- process one value at a time
- avoid storing everything
- work with a long or unknown amount of data

Example:

```python
numbers = [1, 2, 3]
print(numbers[0])
print(len(numbers))
```

A generator does not support indexing or `len`.

## Common Mistakes
- Calling a generator function and expecting the body to run immediately.
- Trying to use the same generator twice.
- Trying to index a generator.
- Forgetting that `yield` pauses the function.
- Using a generator when a simple list would make the code clearer.

## Summary
- A generator produces values one at a time.
- A generator function uses `yield`.
- Calling a generator function returns a generator object.
- Generators are one-time use.
- Generator expressions use parentheses.
- Use generators when you want lazy, memory-friendly iteration.
