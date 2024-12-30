import math
lower = int(input("Enter the lower lt: "))
upper = int(input("Enter the upper lt: "))
for num in range(lower, upper+1):
    count = len(str(num))
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum += pow(digit,count)
        num //= 10
    if  temp == sum:
        print(temp)