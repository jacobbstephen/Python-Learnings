name = input("Enter the name: ")
mark1 = int(input("Enter Mark1: "))
mark2 = int(input("Enter Mark2: "))
mark3 = int(input("Enter Mark3: "))

total_marks =  mark1 + mark2 + mark3
total_percentage = (total_marks / 300 ) * 100
if total_percentage > 50: 
    print("pass")
else: 
    print("fail")