# if-elif-else statement

age = 25

if age <=12:
    print('Kid')
elif age <= 19:
    print('teenager')
elif age <= 35:
    print('Young adult')
else:
    print('Adult')

# Ternary Operator
age = 19
voter = "Adult" if age >=18 else "Minor"
print(voter)


# Match-Case Statement
number = 1
# match number: # require python 3.10+
#     case 1: 
#         print("one")
#     case 2 | 3:
#         print("Two or Three")
#     case _:
#         print("Other number")