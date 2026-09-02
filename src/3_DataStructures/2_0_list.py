"""
Lists in Python

"""

# List is a built-in data structure used to store ordered collection of items.
# they are dynamic, resizable and capable of storing elements of different type

# Creating a list
a = [1, 2,3]
print(a) # [1, 2, 3]

b = list((4,5,6))
print(b) # [4, 5, 6]

print([1]*3) # 1, 1, 1]


# Accessing elements
a = [1,2 ,3]
print(a[0])
print(a[-1])

# Adding elements
a = [1,2,3]
a.append(4)
print(a)

a.insert(1, 2)
print(a)

a.extend([10, 20, 30])
print(a)

# Updating elements
a = [1,2,3]
a[1] = 10
print(a)


# Removing the elements
# Removes the first occurrence of element
a = [1,2,3]
a.remove(2)
print(a) # [1, 3]

# del
del a[1]
print(a) # [1]

# clear
# clear removes all elements
a.clear()
print(a)


# iterating over lists
fruits = ['apple', 'banana', 'fruit']
for fruit in fruits:
    print(fruit)

# Nested Lists
# A nested list is a list it contains another list as its element
a = [[1, 2,3]]
print(a[0])
print(a[0][1])

# List comprehension
# Concise way to create new elements by applying expression on each  item in an existing iterable
elements = [1, 2, 3]
double = [element*2 for element in elements]
print(double)


# List comprehension can use conditions to select or transform items 
# based on specific rules
numbers = [1, 2, 3, 4, 5]
primes = [number for number in numbers if number % 2 == 0]
print(primes)

# using if-else
numbers = [1, 2, 3, 4]
eveodd = ["EVEN" if number % 2 == 0 else "ODD" for number in numbers]
print(eveodd)


# Examples
# 1 Create a list from range
elements = [element for element in range(5)]
print(elements) # [0, 1, 2, 3, 4]

# 2 Using nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)

# 3 Flattening a list of lists
mat = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
elements = [element for row in mat for element in row]
print(elements)
