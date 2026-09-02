"""
Iterating over loops
"""

# enumerate
# It is useful when you need both index and corresponding element while iterating
# through a list

elements = [1, 2, 3]
for index, element in enumerate(elements):
    print(f"Index: {index}, element:{element}")

# Using while loop
elements = [1, 2, 3, 4]
index = 0
while(index < len(elements)):
    print(elements[index])
    index+=1

# Using range() with for loop
elements = [10, 20, 30]
for element in range(len(elements)):
    print(elements[element])