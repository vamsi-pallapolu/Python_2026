# union()
# intersection()
# intersection_update()
# difference()
# difference_update()
# symmetric_difference()
# symmetric_difference_update()
# isdisjoint()
# issubset()
# issuperset()

# union
s1 = {1, 2, 3}
s2 = {2, 3,4}
result = s1.union(s2)
print(result) # {1, 2, 3, 4}

# intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
result = s1.intersection(s2)
print(result) # {2, 3}
print(s1) # {1, 2, 3}

# intersection_update
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.intersection_update(s2)
print(s1) # {2, 3}

# difference
s1 = {1, 2, 3}
s2 = {2, 3, 4}
result = s1.difference(s2)
print(result) # {1}
print(s1) # {1, 2, 3}   

# difference_update
s1 = {1, 2, 3}
s2 = {2, 3, 4}     
s1.difference_update(s2)
print(s1) # {1}

# symmetric_difference
s1 = {1, 2, 3}
s2 = {2, 3, 4}
result = s1.symmetric_difference(s2)
print(result) # {1, 4}
print(s1) # {1, 2, 3}

# symmetric_difference_update
s1 = {1, 2, 3}
s2 = {2, 3, 4}    
s1.symmetric_difference_update(s2)
print(s1) # {1, 4}

# isdisjoint
s1 = {1, 2, 3}
s2 = {4, 5, 6}
result = s1.isdisjoint(s2)
print(result) # True

# issubset
s1 = {1, 2}
s2 = {1, 2, 3, 4}
result = s1.issubset(s2)
print(result) # True

# issuperset
s1 = {1, 2, 3, 4}
s2 = {1, 2}
result = s1.issuperset(s2)
print(result) # True

