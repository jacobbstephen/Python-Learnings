year = int(input("Enter the year: "))
if ((year % 400 == 0) and (year % 100 == 0)) or ((year % 4 == 0) and (year % 100 != 0)):
    print("{0} is a leap year".format(year))
else:
    print("Not a leap Year")