
def TestUnique(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
    

def DataInput(list):
    n = int(input("How many data?_"))
    i = 0
    while i < n:
        data = int(input("Enter number: "))
        list.append(data)
        i += 1
    print("Data list_is: ", list)


data_list = []
DataInput(data_list)

result = TestUnique(data_list)

if result == True:
    print("All numbers is unique")
else:
    print("All numbers is not unique")