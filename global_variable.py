#Variable are declared outside the function called global

x = "Global variable"

def myFunc():
    print("This is " + x)

myFunc()

#Variable are declared inside a function called local

def MyFunc2():
    x = "Local variable"
    print("This is a " + x)
    
MyFunc2()