def check_pal(str):
    if str == str[::-1]:
        return True
    else:
        return False

list = []
pal = []

n = int(input("Enter no of  strings: "))
for i in range(0,n):
    str = input("Enter the string: ")
    list.append(str)

print(list)

for item in list:
    if check_pal(item):
        pal.append(item)
        
print(pal)