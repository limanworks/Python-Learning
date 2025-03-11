#Variables are declared inside a function called local variable

def myFun():
    x = "Local variable"
    print("This is a " + x)

myFun()

x = "Global variable"
print("This is a " + x)