num = int(input("Enter the number: "))
fact = 1
if  num == 0:
    print("factorial is 1")
else:
    for i in range(1,num + 1):
        fact *= i
    print("Factorial is {0}".format(fact))