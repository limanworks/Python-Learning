

item=[42, 54, 63, 70, 8, 35, 23]

print(item[0])
print(item[-1])
print(20 in item)
print(45 not in item)
print(item+[33, 53])
print(item)
print(len(item))
item.append(90)
print(item)
item.insert(3,66)
print(item)
item.remove(63)
print(item)
item.sort()
print(item)
item.reverse()
print(item)
item.pop()
print(item)
item2=item.copy()
print(item2)
pos=item2.index(42)
print(pos)
item2.append(54)
count=item2.count(54)
print(count)
item.clear()
item.append(100)
print(item)