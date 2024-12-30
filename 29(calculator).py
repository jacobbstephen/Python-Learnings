def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

print("Select Operation")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
list = [1,2,3,4]
while True:
    
    choice = int(input("Enter choice: "))
    if choice in (1,2,3,4):
        try:
            num1 = float(input("Enter num1: "))
            num2 = float(input("Enter num2: "))
        except ValueError :
            print("Enter a valid Number")
            continue
        if choice == 1:
            print("Sum: ",add(num1,num2))
        elif choice == 2:
            print("Diff: ",sub(num1,num2))
        elif choice == 3:
            print("Mul: ",mul(num1,num2))
        elif choice == 4:
            print("Div: ",div(num1,num2))
        next = input("Do u want enter another operation: ")
        if next == "no":
            break
    else:
        print("Invalid operation")
             