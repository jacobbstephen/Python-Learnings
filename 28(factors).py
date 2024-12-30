def print_factors(n):
    print("The factor's of {0} are".format(n))
    for i in range(1,n + 1):
        if n % i == 0:
            print(i)
num = int(input("Enter the number: "))
print_factors(num)