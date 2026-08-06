import random

# list

l1 = ['apple', 1, 3.4]
print(l1)
l1[1] = 5
print(l1)

# tuple
t = (1, 2, 3)
# t[1] = 4 # TypeError: 'tuple' object does not support item assignment
print(t[1])


# set
chars = {'a', 'b', 'b', 'c'}
for char in chars:
    print(char) 

# cannot access using index
# chars[1] # TypeError: 'set' object is not subscriptable

# dictionary
numbers = {1: 'One', 2: 'two'}
for number in numbers:
    print(numbers[number])

# random numbers
print(random.randint(1, 5))
print(random.uniform(1, 10))

import math

print(math.nan)
print(float('inf'))
print(float('-inf'))


# convert integer to a string
# Method 1
n = 4
s = str(n)
print(type(s))

# Method 2
m = 2
s2 = f"{m}"
print(s2)
print(type(s2))

# Method 3 - Using format function
o = 3
s3 = "{}".format(n)
print(type(s3))


# Handling invalid input string
try:
    s = "hello"
    n = int(s)
except ValueError:
    print(f"Invalid input \"{s}\", cannot convert to integer")

s1 = 'hi'
if s1.isdigit():
    n = int(s1)
    print(n)
else:
    print("The string is not numeric")