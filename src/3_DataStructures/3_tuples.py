"""
tuples

A tuple is an immutable ordered collection of items

"""

# Creating a tuple
t = ()
print(t)
print(type(t))

t = ('hello', 'world')
print(t)

t = tuple('Geek')
print(t)

# to create one element tuple
t =(10,)
print(t) #(10,)
print(type(t)) 

# Accessing tuples
t = (1, 2, 3, 4)
print(t[0]) # 1
print(t[1:len(t)]) # (2,3, 4)
print(t[:4]) # (1, 2, 3, 4)


# tuple packing
a = 1, 'hello', True
print(a) # (1, 'hello', True)


# tuple unpacking
t = ('Geek', 'for', 'geeks')
word1, word2, word3 = t
print(word1)
print(word2)
print(word3)

## tuple unpacking with asterik
a, *b , c = (1,2,3,4,5)
print(a) # 1
print(b) # [2,3,4]
print(c) # 5


# Concatenation
tuple1 = (1,2,3)
tuple2 = ('hi', 'hello', 'world')
tuple3 = tuple1 + tuple2
print(tuple3)


# count
tuple1 = (1, 1, 2,2,3, 4,4)
print(tuple1.count(1)) # 2

# index
tuple1 = (1, 2, 3, 4, 5)
print(tuple1.index(3)) # 2

# deleting a tuple
tuple1 = (1, 2, 3, 4, 5)
del tuple1
# print(tuple1) # NameError: name 'tuple1' is not defined

######## reversing tuple ###############
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[::-1])

# Using reversed() funtion returns an iterator that can be converted to tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple(reversed(tuple1)))
print(list(reversed(tuple1)))

# Using loop
tuple1 = (1, 2,3)
for i in range(len(tuple1)-1, -1, -1):
    print(tuple1[i])

# Using comprehension
result = tuple(tuple1[i] for i in range(len(tuple1)-1, -1, -1))
print(result) # (3, 2, 1)

########### Tuples to dict #################
# using dict()
l = [(1, "one"), (2, "two")]
d = dict(l)
print(d)

# Using dictionary comprehension
res = {key: value for key, value in l}
print(res)


# Using for loop
d = {}
for key, value in l:
    d[key] = value
print(d)

