"""
Dictionary comprehensions

- It is used to create a dictionary in a short and clear way.
- It allows keys and values to be generated from a loop in single line

"""

d = {x: x*2 for x in range(1, 5)}
print(d)


# Creating dictionary using two lists

l1 = ['a', 'b', 'c', 'd', 'e', 'f']
l2 = [1, 2, 3, 4, 5]
d = {k:v for (k, v) in zip(l1, l2)}
print(d)

# fromkeys() method
d = dict.fromkeys(range(5), True)
print(d) # 0: True, 1: True, 2: True, 3: True, 4: True}

# EXAMPLES

## Example 1

d = {c: "Char" for c in "wor123&*" if c.isalpha()}
print(d)

## Example 2
d = {fruit: len(fruit) for fruit in ['apple', 'banana', 'mango']}
print(d)

######### Nested Dictionary Comprehension ##############
s = "GF"
d = {x:{y : x+y for y in s } for x in s}
print(d) # {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}