class MyException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

err = MyException("My Error Message")
print(err)

class MyException2(Exception):
    def __init__(self, message: str, errorCode: int):
        super().__init__(message)
        self.message = message
        self.errorCode = errorCode

    def __str__(self):
        return f"{self.message}, (errorCode: {self.errorCode})"

err2 = MyException2("Error Message 2", 400)
print(err2)


# Raising a custom exception
def divide(num1: int, num2: int):
    if(num2 == 0):
        raise MyException("Divide By Zero Error")
    return num1/num2

divide(3, 3)

# Handling Custom Exception
try:
    divide(3, 0)
except MyException as e:
    print(e)
