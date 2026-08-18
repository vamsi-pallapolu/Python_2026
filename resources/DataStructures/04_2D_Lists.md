# 2-D Lists

Source: `DataStructures/2_2_2d.py`

## What is a 2-D list?
A 2-D list is a **list of lists** — think a grid or table. Each inner list is a row, and you access a cell with `matrix[row][col]`. It's how you represent matrices in Python.

## Creating a 2-D list
Literal form — a list of row lists:
```python
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a)
```

## Building a zero matrix with nested loops
Build an `m × n` matrix filled with zeros by appending rows one at a time.
```python
m, n = 4, 5
mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)
print(mat)
```
Each iteration creates a **new** inner list, so rows are independent. Avoid `[[0] * n] * m` — it repeats the *same* row reference `m` times, and mutating one row mutates all. A comprehension (`[[0] * n for _ in range(m)]`) is the concise, correct one-liner.

## Iterating row-by-row
Iterating a 2-D list directly yields each row (an inner list).
```python
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in a:
    print(row)
```

## Index-based nested loops
When you need both the row and column indices (e.g. to modify in place, or print the element at `[i][j]`), loop over the index ranges.
```python
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    print()
```
Using `len(a[i])` (not `len(a[0])`) makes this safe for jagged lists where rows have different lengths.

## Methods on the outer vs inner list
Every list method works at the level you call it — the outer list treats each row as a single element, while `a[i]` operates on that specific row.

**`append` on the outer list — adds a new row:**
```python
a = [[1, 2], [3, 4]]
a.append([6, 7])
# [[1, 2], [3, 4], [6, 7]]
```

**`extend` on a row — grows that row:**
```python
a[0].extend([0, 0])
# [[1, 2, 0, 0], [3, 4], [6, 7]]
```

## Reversing rows vs the whole matrix
`reverse()` is in-place and only reverses the list it's called on.
```python
a = [[1, 2], [3, 4]]
a[0].reverse()      # [[2, 1], [3, 4]]  — only row 0 is reversed
a.reverse()         # [[3, 4], [2, 1]]  — the row order is reversed
```
This is not a transpose — swapping rows and columns needs a separate step (`list(zip(*a))` or a nested comprehension).

## List comprehension over a 2-D list
Nest a comprehension inside another to transform each element of each row while preserving structure.
```python
a = [[1, 2], [2, 3]]
r = [[x * 2 for x in row] for row in a]
# [[2, 4], [4, 6]]
```
The **outer** comprehension iterates rows; the **inner** one builds a new row from that row's elements. To *flatten* instead of preserving structure, put both `for` clauses in one comprehension: `[x for row in a for x in row]`.

## Common patterns
| Task | Idiom |
|------|-------|
| Build `m × n` zero matrix | `[[0] * n for _ in range(m)]` |
| Access element | `a[i][j]` |
| Number of rows / cols | `len(a)` / `len(a[0])` (assumes rectangular) |
| Iterate rows | `for row in a:` |
| Iterate elements with indices | `for i, row in enumerate(a): for j, x in enumerate(row):` |
| Transform every element | `[[f(x) for x in row] for row in a]` |
| Flatten to 1-D | `[x for row in a for x in row]` |
| Transpose | `list(map(list, zip(*a)))` |

## Gotchas
- **`[[0] * n] * m` shares the row** — all `m` "rows" point to the same inner list; mutating one mutates all. Use a comprehension instead.
- **Shallow copies still share inner rows** — `a.copy()`, `list(a)`, and `a[:]` copy the outer list only. Use `copy.deepcopy(a)` when you need independent rows.
- **`reverse()` returns `None`** — it mutates in place. `b = a.reverse()` sets `b` to `None`; use `a[::-1]` for a reversed copy.
- **Jagged rows break `len(a[0])`-based loops** — always index off `a[i]` when row lengths may vary.
- **`append` vs `extend` on a row** — `row.append([0, 0])` adds one nested element (`[..., [0, 0]]`), while `row.extend([0, 0])` adds the two ints individually.
