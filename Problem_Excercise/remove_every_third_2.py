
def RemoveThird(x):
    position = 2
    index = 0
    size = len(x)
    ctr = 0

    while size > 0:
        ctr += 1
        index = (position + index) % size
        x.pop(index)
        print("Step-", ctr, ": ", x)
        size -= 1


def NumberInput(x):
    i = 0
    while i < 10:
        n = int(input("Enter number: "))
        list.append(n)
        i += 1
    print("List_is: ", x)


list = []


NumberInput(list)
RemoveThird(list)




