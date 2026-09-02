# same value can be assigned to multiple variables in the same line

a = b = c = 20

print(a, b, c)


# Assigning different variables with differnt values in the same line
x, y, z = "vamsi", 29, "mathworks"
print(x, y, z)


# Importnat notes

"""
Python variables store references to object not the actual values

"""

x = 1
y = x
y = y + 1
print(x)
print(y)

# deletion of variable

z = 30
del z
# print(z)


# Lists

v1 = [1, 2, 3]
v2 = [1, 2 , 3]

print(id(v1))
print(id(v2))


# Practical examples
# 1 Swapping two variables

a, b = 10, 20
a, b = b, a


# counting characters in a string
word = "Python"
length = len(word)
print("Length of word", length)

