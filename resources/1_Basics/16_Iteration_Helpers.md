# Iterators and Iteration Helpers

## Definition
An **iterable** is something you can loop over.

Examples:

```python
names = ["Asha", "Ben", "Carlos"]
text = "Python"
numbers = range(3)
```

An **iterator** is the object that gives values one at a time.

```python
items = iter(["a", "b", "c"])

print(next(items))
print(next(items))
print(next(items))
```

Output:

```text
a
b
c
```

After the last item, `next(items)` raises `StopIteration`.

## How a `for` Loop Works
A `for` loop handles `iter()` and `next()` for you.

```python
for name in ["Asha", "Ben", "Carlos"]:
    print(name)
```

Roughly means:

```python
items = iter(["Asha", "Ben", "Carlos"])

while True:
    try:
        name = next(items)
    except StopIteration:
        break

    print(name)
```

You usually write the `for` loop.

## One-Time Iterators
Many iterators can be used only once.

```python
items = iter([1, 2, 3])

print(list(items))
print(list(items))
```

Output:

```text
[1, 2, 3]
[]
```

The iterator was empty the second time.

## The `range` Function
`range` gives numbers without building a full list.

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

Useful forms:

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 6)     # 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

## The `enumerate` Function
Use `enumerate` when you need both the index and the value.

```python
names = ["Asha", "Ben", "Carlos"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

Output:

```text
1 Asha
2 Ben
3 Carlos
```

This is usually clearer than `range(len(names))`.

## The `zip` Function
Use `zip` to loop over multiple iterables at the same time.

```python
names = ["Asha", "Ben"]
scores = [95, 88]

for name, score in zip(names, scores):
    print(name, score)
```

Output:

```text
Asha 95
Ben 88
```

By default, `zip` stops at the shortest input.

```python
list(zip([1, 2, 3], ["a", "b"]))
```

Result:

```python
[(1, "a"), (2, "b")]
```

Use `strict=True` when different lengths should be an error.

```python
list(zip([1, 2, 3], ["a", "b"], strict=True))
```

## The `sorted` Function
`sorted` returns a new sorted list.

```python
numbers = [3, 1, 2]
print(sorted(numbers))
print(numbers)
```

Output:

```text
[1, 2, 3]
[3, 1, 2]
```

Use `key` to say how items should be sorted.

```python
words = ["banana", "fig", "apple"]
print(sorted(words, key=len))
```

Output:

```text
['fig', 'apple', 'banana']
```

## The `map` and `filter` Functions
`map` applies a function to each item.

```python
numbers = [1, 2, 3]
print(list(map(str, numbers)))
```

Output:

```text
['1', '2', '3']
```

`filter` keeps items that pass a test.

```python
numbers = [1, 2, 3, 4]

def is_even(number):
    return number % 2 == 0

print(list(filter(is_even, numbers)))
```

Output:

```text
[2, 4]
```

List comprehensions are often easier to read:

```python
print([number for number in numbers if number % 2 == 0])
```

## Useful `itertools` Helpers
Join iterables:

```python
from itertools import chain

print(list(chain([1, 2], [3, 4])))
```

Output:

```text
[1, 2, 3, 4]
```

Take part of any iterable:

```python
from itertools import islice

numbers = range(100)
print(list(islice(numbers, 5)))
```

Output:

```text
[0, 1, 2, 3, 4]
```

Create pairs:

```python
from itertools import pairwise

print(list(pairwise(["a", "b", "c"])))
```

Output:

```text
[('a', 'b'), ('b', 'c')]
```

## Common Mistakes
- Forgetting that iterators can be exhausted.
- Using `range(len(items))` when `enumerate(items)` is clearer.
- Forgetting that `zip` stops at the shortest iterable.
- Expecting `map`, `filter`, or `zip` to return a list. Use `list(...)` if you need a list.
- Using advanced `itertools` tools before a simple loop is understood.

## Summary
- Iterables can be looped over.
- Iterators produce values one at a time.
- Many iterators are one-time use.
- `range`, `enumerate`, `zip`, `sorted`, `map`, and `filter` help with common loop patterns.
- Prefer clear loops and comprehensions when they are easier to read.
