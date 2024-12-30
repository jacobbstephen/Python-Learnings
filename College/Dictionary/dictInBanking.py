def deposit(dict):
    name = "jacob"
    amount = 500
    dict[name] += amount
    print(dict) 
    
def withdraw(dict):
    name = "rosh"
    amount = 5000
    dict[name] -= amount
    print(dict)

dict = {"jacob": 4500,"rosh": 10000}

choice = int(input("Enter the choice: "))
if choice == 1:
    withdraw(dict)
else: 
    deposit(dict)