# Iteration

Source: `DataStructures/2_1_iteration.py`

## What is iteration?
Iteration is the process of stepping through the elements of an **iterable** (list, tuple, string, dict, set, generator, `range`, ...) one at a time. Python's canonical iteration construct is the `for` loop, which internally calls `iter()` on the iterable and then `next()` repeatedly until `StopIteration` is raised. `while` loops are used when the stopping condition isn't tied to a sequence — e.g. index-based traversal, waiting on a state change, or reading until a sentinel value.

## `for ... in` — the default
Iterates directly over elements. No manual index tracking needed.
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

## `enumerate` — index + element
Use when you need **both** the index and the value. Cleaner and faster than `range(len(...))`.
```python
elements = [1, 2, 3]
for index, element in enumerate(elements):
    print(f"Index: {index}, element:{element}")
```
Optional `start` argument sets the first index:
```python
for i, ch in enumerate("abc", start=1):
    print(i, ch)          # 1 a / 2 b / 3 c
```

## `while` loop — condition-driven
Repeats as long as a condition is true. Useful when the loop doesn't map cleanly to a sequence.
```python
elements = [1, 2, 3, 4]
index = 0
while index < len(elements):
    print(elements[index])
    index += 1
```
Python uses `index += 1` to increment — there is **no** `++` or `--` operator. Writing `index++` is a syntax error; `++index` is parsed as unary `+` applied twice — it evaluates `index` but does not increment it, so it's a misleading no-op and shouldn't be used.

## `range(len(...))` — index-based `for`
Iterate by index without a `while` loop.
```python
elements = [10, 20, 30]
for i in range(len(elements)):
    print(elements[i])
```
This works but is often not the best choice — prefer:
- `for x in elements:` when you only need values.
- `for i, x in enumerate(elements):` when you need **both** index and value (no double lookup).
Reach for `range(len(...))` only when you truly need just the indices (e.g. modifying elements in place by index, or iterating in step with another sequence via a shared index).

## `for` vs `while` — when to use which
| Use `for` when... | Use `while` when... |
|---|---|
| Iterating over a known iterable | Loop end depends on runtime state, not a sequence |
| You want every element | You're polling / retrying / waiting for a condition |
| Idiomatic, most common case | Index-based logic with skips or resets |

Even for index-based traversal, prefer `for i in range(len(...))` or `enumerate` — reserve `while` for genuinely condition-driven loops.

## Loop control keywords
| Keyword | Effect |
|---------|--------|
| `break` | exit the enclosing loop immediately |
| `continue` | skip to the next iteration |
| `pass` | no-op placeholder (not loop-specific) |
| `else` on a loop | runs **only if the loop finished without `break`** |

```python
for n in [1, 2, 3, 4]:
    if n == 3:
        break
else:
    print("completed")     # not printed — broke out early
```

## Iterating other common types
```python
# String — one character at a time
for ch in "abc":
    print(ch)

# Dict — keys by default; use .items() for pairs
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)

# range — lazy sequence of ints
for i in range(3):
    print(i)               # 0, 1, 2
```

## Iterables vs iterators (quick note)
- An **iterable** is anything you can call `iter()` on (list, str, dict, set, generator, ...).
- An **iterator** is the object returned by `iter()` — it has `__next__()` and yields values until `StopIteration`.
- `for` handles both transparently; you rarely call `iter` / `next` directly.

## Gotchas
- **Modifying a list while iterating over it** can skip or repeat elements. Iterate over a copy (`for x in a[:]`) or build a new list.
- **`range(len(x))` when you also need the value** — use `enumerate(x)` instead.
- **No `++` / `--` in Python** — always `x += 1`. Integers are immutable, so `+=` rebinds the name to a new int object.
- **Infinite `while` loops** — forgetting to update the loop variable is the classic bug (`while index < n:` with no `index += 1`).
- **Loop variable leaks** — after `for i in range(3): ...`, `i` is still bound to `2` outside the loop. Python does not scope regular `for`-loop variables to the loop body. **Comprehension** loop variables (`[x for x in ...]`), on the other hand, **are** scoped to the comprehension in Python 3 — they do not leak.
