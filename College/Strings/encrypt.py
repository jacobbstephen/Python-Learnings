str = input("Enter the string: ")
key = int(input("Enter the key: "))

for i in str:
    if ord(i) + key > ord('z'):
        # ordval = ord('a') + key - (ord('z') - ord(i) + 1)
        ordval = key - 26 + ord(i)
        print(chr(ordval), end = "")
    else:
        print(chr(ord(i) + key), end = "")
# print(ord('z'))
