import math
num = int(input("Enter the number: "))
temp = num
count = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum += pow(digit,count)
    num //= 10
if sum == temp:
    print("{0} is amstrong".format(temp))
else:
    print("Not Amstrong")