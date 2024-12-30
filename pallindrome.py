str = input("Enter the string: ")
str = str.casefold()
rev = str[::-1]
print(rev)
if str == rev: 
    print("pallindrome")
else:
    print("Not pallindrome")