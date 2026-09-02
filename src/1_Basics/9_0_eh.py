"""
Exception Handling in python

"""

try:
    n = 0
    res = 10/3
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("The result is:", res)
finally:
    print("Execution completed")


# Specific Exception handling
try:
    x = int("str")
    res = n/x
except ValueError:
    print("Invalid value provided")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("The result is:", res)
finally:
    print("Execution completed")

# Multiple Exceptions
# if we want to handle multiple exceptions in the same way
# or we can sepearte them if we require different handling for each exception
a = ["10", "twenty", 30]
try:
    res = int(a[0]) + int(a[1])
except (ValueError, TypeError) as e:
    print("Error occurred:", e)
else:
    print("The result is:", res)
finally:
    print("Execution completed")


# catch all exceptions
try:
    res = 10/0
except Exception as e:
    print("An error occurred:", e)


# Raise an exception
def age(age):
    if(age <0):
        raise ValueError("Age cannot be negative")
    print(age)

try:
    age(-5)
except ValueError as e:
    print("Error occurred:", e)