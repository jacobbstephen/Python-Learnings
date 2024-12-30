n1 = int(input("ENter n1"))
n2 = int(input("ENter n2"))
n3 = int(input("ENter n3"))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the largest")
elif n2> n1 and n2 > n3:
    print(f"{n2} is the largest")
else:
    print(f"{n3} is the largest")