# example
def evenOdd(x):
    if x%2 == 0:
        print("Even")
    else:
        print("Odd")

evenOdd(10)

# default arguments
def fun(arg1, arg2=40):
    print(arg1)
    print(arg2)
fun(10)

# Keword arguments
# Passing values through argument names, so argument order does not matter

def student(fname, lname):
    print(fname, lname)

student(fname= 'vamsi', lname = 'pallapolu')
student(lname= 'pallapolu', fname = 'vamsi')

# Arbitraray arguments
# *args stores positional arguments as tuple
def myFun(*args, **kwargs):
    print("Extra Args")
    for arg in args:
        print(arg)

    print("Extra Keyword Args")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

myFun('hello', 'world', fname='vamsi', lname='pallapolu')

# Pass by object-reference

def myFun(x):
    x[0]=20

list = [10,20,30]
myFun(list)
print(list) # 20 20 30

def myFun(a):
    a = 20
a = 10
myFun(a)
print(a)

