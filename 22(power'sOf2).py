import math
terms = int(input("Enter the terms: "))
# mapfn:             (fn here lambda): iterable here range
result = list((map(lambda x: math.pow(2,x),range(terms))))
print(result)