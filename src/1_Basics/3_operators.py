a = 15
b = 4

print("Division", a/b)
print("Floor Division", a//b)
print("Modulus", a%b)
x = 3
y = 3
print("Exponentiation", x**y)

# Relational/Comparison Operators
a = 13
b = 12

print(a<b)
print(a==b) # False
print(a>=b) # True


# Logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not b)


# Bitwise operators 
# & | ~ ^ >> <<

# Assignment Operators
# =, +=, -=, *=, /=, <<=

# Identity Operators
# To check the values are located on same part of the memory
print("~~~~ Identity Operators ~~~~")
a = 10
b = 20
c = a
print(a is not b)
print(a is c)

# Membership Operators
# Used to test whether a value or variable is in a sequence
x = 24
y = 20
my_list = [10, 20, 30, 40]
if ( x in my_list):
    print(f"x:{x} is in my_list")
else:
    print(f"x:{x} is not in my_list")

for x in my_list:
    print(f"x: {x}")

# Ternary operator
print("~~~~ Ternary Operator ~~~~")
a, b = 10, 20
min = a if a < b else b
print(min)


# Operator precedence

# Operator associativity
print(2**3**2) # 512