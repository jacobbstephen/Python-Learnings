import math
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

s = (a + b + c) / 2
d = s * (s - a) * (s - b) * (s - c)
area = round(math.sqrt(d), 2)
print("The area of the triangle is: ",area)