

def RemoveNum(num_list):
    position = 3 - 1
    idx = 0
    list_len = len(num_list)

    while list_len > 0:
        idx = (position + idx) % list_len
        print(num_list.pop(idx))
        list_len -= 1


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#RemoveNum(numbers)

