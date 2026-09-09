import calc

print(calc.add(1, 3))

########### Types of imports #################

from calc import sub
print(sub(3,2)) # Here the prfix calc is not required


# import all names
from calc import *
print(add(1, 3))
print(sub(2, 3))

# import with alias
from calc import add as a
print(a(1, 2)) # 3

import calc as c
print(c.add(10, 10)) # 20

########### Types of modules ###################
# 1. Built-in modules
# These come bundled with Python and require no installation eg: math, random, os

import random
print(random.randint(1, 5)) # 3

# 2. User defined modules
import calc
print(calc.sub(10, 5)) # 5

# 3. Third party modules
# These modules are installed using pip - eg: Numpy, Pandas, Requests
# import requests
# r = requests.get("https://google.com")
# print(r.status_code)


# 4. Package modules
from mypkg import mymath # Loading a module from a package
print(mymath.sub(5,5)) # 0

from mypkg.mymath import add # Loadinga function from module inside a package
print(add(2,5)) # 7


# 5. Location a module
import sys
for p in sys.path:
    print(p)

import mypkg
for p in mypkg.__path__:
    print(p)