# 2-D Lists

Source: `DataStructures/2_2_2d.py`

## Definition
A 2-D list is a **list of lists** — a grid where each inner list is a row. Access a cell with `mat[i][j]`. Python has no built-in matrix type; a nested `list` is the standard structure.

## Creation
Literal form — a list of row lists:
```python
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
```
Nested-loop build:
```python
m, n = 4, 5
mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)
```
Comprehension — the idiomatic form:
```python
mat = [[0] * n for _ in range(m)]
```

## Why `[[0] * n] * m` fails
`* m` repeats the same **reference** `m` times — every row is the same inner list. Mutating one row mutates all.
```python
mat = [[0] * 3] * 2
mat[0][0] = 9
mat        # [[9, 0, 0], [9, 0, 0]]   -- shared row
```
The comprehension `[[0] * n for _ in range(m)]` builds a fresh list each iteration.

## Iterating rows
Iterating a 2-D list yields each row (an inner list).
```python
for row in mat:
    print(row)
```

## Index-based traversal
Use when you need `i` and `j` (in-place updates, printing coordinates). Index off `mat[i]` — not `mat[0]` — so jagged rows still work.
```python
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j])
```

## Row vs matrix operations
Every list method works at the level you call it — `mat.method(...)` acts on the outer list; `mat[i].method(...)` acts on that row.

**Add a row:**
```python
mat.append([6, 7])          # new row at the end
```
**Grow a row:**
```python
mat[0].extend([0, 0])       # appends two ints to row 0
```
**Reverse a row vs reverse row order:**
```python
mat[0].reverse()            # reverses row 0 in place
mat.reverse()               # reverses the order of rows
```
Neither is a transpose — see below.

## Row swap
Tuple unpacking swaps **references**, not contents. Cheap and safe.
```python
mat[i], mat[j] = mat[j], mat[i]
```

## Transpose
Rows and columns are not symmetric — swapping needs `zip`.
```python
mat = [[1, 2, 3], [4, 5, 6]]
list(zip(*mat))                    # [(1, 4), (2, 5), (3, 6)]
list(map(list, zip(*mat)))         # [[1, 4], [2, 5], [3, 6]]
```

## Comprehension patterns
**Transform each element, preserving structure:**
```python
[[x * 2 for x in row] for row in mat]
```
**Flatten to 1-D:**
```python
[x for row in mat for x in row]
```
Nested `for` clauses read left-to-right — outer loop first.

## Common idioms
| Task | Idiom |
|------|-------|
| Zero matrix `m x n` | `[[0] * n for _ in range(m)]` |
| Access element | `mat[i][j]` |
| Dimensions (rectangular) | `len(mat)`, `len(mat[0])` |
| Iterate rows | `for row in mat:` |
| Iterate with indices | `for i, row in enumerate(mat): for j, x in enumerate(row):` |
| Transform elements | `[[f(x) for x in row] for row in mat]` |
| Flatten | `[x for row in mat for x in row]` |
| Transpose | `list(zip(*mat))` |
| Rotate 90° clockwise | `list(zip(*mat[::-1]))` |

## When to use NumPy
For numeric work at scale, `numpy.ndarray` beats a nested list — contiguous memory, vectorized operations, and true multi-dimensional indexing (`a[i, j]` instead of `a[i][j]`). Use nested lists for small, heterogeneous, or non-numeric grids.

## Gotchas
- **`[[0] * n] * m` shares rows** — always use the comprehension form.
- **Shallow copy shares inner rows** — `mat.copy()`, `list(mat)`, `mat[:]` copy the outer list only. Use `copy.deepcopy(mat)` for independent rows.
- **`reverse()` returns `None`** — it mutates. `b = mat.reverse()` sets `b` to `None`; use `mat[::-1]` for a reversed copy.
- **Jagged rows break `len(mat[0])` loops** — index off `mat[i]` when rows may differ in length.
- **`append` vs `extend` on a row** — `row.append([0, 0])` adds one nested list (`[..., [0, 0]]`); `row.extend([0, 0])` adds two ints.
- **Transpose is not `reverse`** — reversing swaps row order; transposing swaps axes.
