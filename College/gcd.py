a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    sma = b
else:
    sma = a

for i in range(1,sma+1):
    if a%i == 0 and b % i == 0:
        gcd = i

print(gcd)