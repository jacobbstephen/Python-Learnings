
n = int(input("Enter the total elements for the list: "))
lst = []
d = int(input("Enter the no: "))
for  i in range(n):
    ele = int(input("enter the elemnt for list: "))
    lst.append(ele)
result = list(filter(lambda x: (x % d == 0),lst ))
print(result)