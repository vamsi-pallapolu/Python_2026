"""
Dictionary methods

"""
# update
d ={'a':1, 'b':2}
res = d.update({'b':4,'c':3})
print(d) # {'a': 1, 'b': 4, 'c': 3}

# setDefault
d ={'a':1, 'b':2}
d.setdefault('b', 3)
print(d)
d.setdefault('c',4)
print(d) # set new key if it is not already exists

##### Shallow Copy ########
import copy
student = {"name": "Emma",
           "marks": [90, 85, 92]}
student2 = student.copy()
student2["marks"][0] = 88
print(student2) # {'name': 'Emma', 'marks': [88, 85, 92]}
print(student) # {'name': 'Emma', 'marks': [88, 85, 92]}

##### Deep Copy ###########
student = {"name": "Emma",
           "marks": [90, 85, 92]}
student3 = copy.deepcopy(student)
student3["marks"][0] = 88
print(student3) # {'name': 'Emma', 'marks': [90, 85, 92]}
print(student) # {'name': 'Emma', 'marks': [88, 85, 92]}