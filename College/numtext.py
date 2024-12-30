f = open("numbers.txt","w")
print("Enter 5 numbers")
for i in range(0,5):
    num = int(input())
    num_str = str(num)
    f.write(num_str + " ")
    
f.close()
f = open("numbers.txt","r")

list = (f.read()).split()
num_list = []
for item in list:
    num = int(item)
    num_list.append(num)
num_list.sort()
print(num_list)

f.close()

sec = open("second.txt","w")
for item in num_list:
    num_str = str(item)
    sec.write(num_str + " ")
