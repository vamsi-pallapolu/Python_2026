# Creating a string

name = 'Vamsi123@*()'
print(name)

# Accessing a string
print(name[1]) # a
print(name[-3]) # *

# String Slicing
s = "abcdef"
print(s[1:4]) # bcd
print(s[:3]) # abc
print(s[3:]) # def
print(s[::-1]) # fedcba

# Looping through strings
s = "ABCDEF"
for char in s:
    print(char)

# String immutability
s = "aBCD"
print(id(s))
s = 'A' + s[1:]
print(s) #ABCD
print(id(s))

# Deleting a string
s = 'vamsi'
del s
# print(s)

# Updating a string
# Strings cannot be changes directly after creation
# Any modification results to a new string being created
# using methods like replace or slicing

s = "abcd"
s1 = "A" + s[1:]
s2 = s.replace("abc", "AB1")
print(s1)
print(s2)

# Common string methods
