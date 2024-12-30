n = [1,4,9]
v = n.__iter__()
item1 = v.__next__()
print(item1)
item2 = v.__next__()
print(item2)
item3 = next(v)# simple way

print(item3)