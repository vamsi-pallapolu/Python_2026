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