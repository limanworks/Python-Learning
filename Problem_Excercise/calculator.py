def Add(a,b):
    return a + b

def Subtract(a,b):
    return a - b

def Multiply(a,b):
    return a * b

def Divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error"
    
def Calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {Add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {Subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {Multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {Divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    Calculator()