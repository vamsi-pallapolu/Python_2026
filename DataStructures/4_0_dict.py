"""
Learning dictionaries

Dictionary is a data struture that stores information in key value pairs.
- Keys are immutable (like int, string), unique
- Values are mutable (like list)
"""

# Creating dictionaries
coordinates = {'x': 1, 'y': 2}
print(coordinates)

person = dict(name="vamsi", age = 21)
print(person)

# Accessing dictionary items
print(person['name'])
print(person.get('age'))


# Adding and Updating dictionary items
person['lastName'] = 'pallapolu'
print(person)

person['age'] = 31
print(person)

# Removing dictionary items
del person['lastName']
print(person)


# pop
person.pop('age')
print(person)

# popitem
person.popitem()
print(person)


# clear
person = dict(name='vamsi', age=31)
print(person)
person.clear()
print(person)



"""
`del` keyword — usage

| Target              | Example                    | Effect                                                  |
|---------------------|----------------------------|---------------------------------------------------------|
| Variable (name)     | `del x`                    | Unbinds the name; later use raises `NameError`.         |
| List item           | `del nums[0]`              | Removes element at index (in-place). Shifts left.       |
| List slice          | `del nums[1:3]`            | Removes a range of elements in-place.                   |
| Dict key            | `del d['k']`               | Removes the key/value pair; missing key → `KeyError`.   |
| Set: not supported  | `del s[x]`                 | `TypeError` — sets have no indexing; use `s.discard(x)`.|
| Attribute           | `del obj.attr`             | Removes the attribute; calls `__delattr__`.             |
| Object index/slice  | `del obj[k]`               | Calls `__delitem__(k)` on the object.                   |
| Multiple targets    | `del a, b, c[0]`           | Applies `del` to each target left-to-right.             |
| Global / nonlocal   | `del x` inside function    | Requires `global x` / `nonlocal x` to affect outer scope.|

Notes:
- `del` does not free memory directly — it decrements the reference count; the object is freed when no references remain.
- Tuples and strings are immutable — `del t[0]` raises `TypeError`.
"""