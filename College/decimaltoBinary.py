dec = int(input("Enter the decimal  no: "))
bin = 0
i = 1
while(dec > 0):
    rem =  dec % 2
    bin += rem*i
    dec //= 2
    i *= 10
    print(bin)


print(bin)