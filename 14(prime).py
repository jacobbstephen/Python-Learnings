num = int(input("Enter the number: "))
flag = True
for i in range(2,num):
    if num % i == 0:
        flag = False
        break
if flag:
    print("{0} is prime".format(num))
else:
    print("{0} is not prime".format(num))