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
# len
s = "Vamsi"
print(len(s))

# upper
s = "hello"
print(s.upper())

# lower
s = "LOWeR"
print(s.lower())

# strip, lstrip, rstrip
s = "   Vamsi P "
print(s.strip())

# replace
s = "Python is fun"
print(s.replace("fun", "awesome"))


# Concatenating and Repeatimg strings
s1 = "Vamsi"
s2 = "Krishna"
print(s1+s2)

# A string can be repeated multiple times using *
print("Hello "*3)

# Formatting Strings
name = "Vamsi"
age = 29
print(f"name is {name}, age is {age}")

print("name: {}, age: {}".format(name, age))

# String Membership Testing
s = "Hello World"
print("Hello" in s) # True


# Comparison 
s1 = "Python"
s2 = "Python"
print(s1 == s2) # True

print(s1 is s2) # True


s = "hello dude"
print(s.startswith("hello")) # True
print(s.endswith("hello")) # False


# Convert a string to list 
s = "Python is a programming language"
words = s.split()
for word in words:
    print(word)

words = list(s)
print(words)

# Custom delimiter
s = "1,2,3"
nums = s.split(',')
for num in nums:
    print(num)

# Using list comprehension
s = "Python"
a = [ch for ch in s]
print(a)