"""
Sets

- Definition: A set is a collection of unique elements. It is an unordered data structure that does not allow duplicate values.
- Operations: Sets support various operations such as union, intersection, difference, and symmetric difference.
     They also allow for membership testing and can be used to remove duplicates from a collection. 
- Implementation: In Python, sets can be created using the built-in `set()` function or by using curly braces `{}`.
     Elements can be added to a set using the `add()` method and removed using the `remove()` or `discard()` methods. 
     Sets can also be iterated over, and they support various set operations through methods like `union()`, `intersection()`, and `difference()`.  
"""

# Creation of a set
s = {1,2, 3, 4, 5,5, 6}
print(s) # {1, 2, 3, 4, 5, 6}

# Accessing
print(s) # {1, 2, 3, 4, 5, 6}
for item in s:
    print(item, end=' ')
try:
    print(s[0])
except TypeError as e:
    print(e) # 'set' object is not subscriptable

# Adding elements
s = {1, 2, 3}
s.add(4)
print(s, end='') # {1, 2, 3, 4}
print()

s.update([4, 5, 5])
print(s) # {1, 2, 3, 4, 5}

# Removing elements
print("$$$$$$$ Removing elements $$$$$$$")
s.remove(5)
print(s) # {1, 2, 3, 4}

s = {1, 2, 3, 4, 5}
try:
    s.remove(6)
except KeyError as e:
    print(f"{e} is not present in set") #

s = {1, 2, 3, 4, 5}
s.discard(6) # does not raise an error if the element is not present
print(s)


s = {1,2 ,3}
s.pop()
print(s)

s=set()
try:
    s.pop()
except KeyError as e:
    print(f"{e} is not present in set") # 'pop from an empty set' is not present in set


"""
Summary of Set methods used in this file:

| Method              | Purpose                                     | Example                     | Behavior on missing element                         |
|---------------------|---------------------------------------------|-----------------------------|------------------------------------------------------|
| set() / {...}       | Create a set (duplicates removed)           | s = {1, 2, 3, 4, 5, 5}      | N/A                                                  |
| add(x)              | Add a single element                        | s.add(4)                    | No-op if already present                             |
| update(iterable)    | Add multiple elements from an iterable      | s.update([4, 5, 5])         | Duplicates ignored                                   |
| remove(x)           | Remove element x                            | s.remove(5)                 | Raises KeyError                                      |
| discard(x)          | Remove element x if present                 | s.discard(6)                | Silent, no error                                     |
| pop()               | Remove and return an arbitrary element      | s.pop()                     | Raises KeyError on empty set                         |
| in                  | Membership test                             | 3 in s                      | Returns False                                        |
| for item in s       | Iterate over elements (unordered)           | for item in s: ...          | N/A                                                  |
| s[i]  (unsupported) | Indexing — not supported                    | s[0]                        | Raises TypeError: 'set' object is not subscriptable  |

Note: s = {} creates an empty dict, not a set — use s = set() for an empty set.
"""
