"""
Dictionary Iterations
"""
# Iterate all keys
d = {'one':1, 'two':2}
for key in d:
    print(key)

# Iterate all values
d = {'one':1, 'two':2}
for value in d.values():
    print(value)

# Iterate key value pairs
d = {'one':1, 'two':2}
for key, value in d.items():
    print(f"Key:{key},Value:{value}")

# Nested dictionaries
d = {
    "student1":{
        'name': 'vamsi',
        'no': 1,
        'age': 18
    },
    "student2":{
            'name': 'krishna',
            'no': 2,
            'age': 18
    }
}

for student, details in d.items():
    print(f"{student} details: ")
    for key, name in details.items():
        print(f"{key}:{name}")

print("Second loop")

for students, details in d.items():
    for detail in d[students].keys():
        print(d[students][detail])
