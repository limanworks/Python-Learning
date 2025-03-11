
num_1=int(input("num_1: "))
num_2=int(input("num_2: "))
num_3=int(input("num_3: "))

if num_1>num_2:
    if num_1>num_3:
        print("num_1 is max")
if num_2>num_1:
    if num_2>num_3:
        print("num_2 is max")
else:
    print("num_3 is max")