num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

if (num1 > num2) and (num1 > num3):
    print("{0} is greatest ".format(num1))
elif (num2 > num1) and (num2 > num3):
    print("{0} is greatest ".format(num2))
else:
    print("{0} is greatest ".format(num3))