str = input("Enter the string: ")
key = int(input("Enter the key: "))

for i in str:
    if ord(i) - key < ord('a'):
        # ordval =   ord('z') + ord(i) + 1 - (ord('a') + key)
        ordval = ord(i) - key + 26
        print(chr(ordval), end = "")
    else:
        print(chr(ord(i) -  key), end = "")