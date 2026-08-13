# Examples

a = [[1,2, 3], [4, 5, 6], [7, 8,9]]
print(a)

# Creating a multidimensional zero matrix
m ,n = 4, 5
mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    mat.append(row)
print(mat)

a = [[1,2, 3], [4, 5, 6], [7, 8,9]]
for row in a:
    print(row)

# Using index based Nestted loops
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    print()

# Methods on multi-dimensional list
a = [[1, 2], [3, 4]]
a.append([6, 7])
print(a)

# Using extend
a[0].extend([0, 0])
print(a)

# reverse
# revers a row
a = [[1, 2], [3, 4]]
a[0].reverse()
print(a)
a.reverse()
print(a)

# using list comprehension for processing rowa
a = [[1, 2], [2, 3]]
r = [[x*2 for x in row] for row in a]
print(r)