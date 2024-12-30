import cmath
# solve ax^2 + bx+ c
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter the constant: "))

d = cmath.sqrt((b**2 - (4*a*c)))
soln1 = (-b + d) / (2 * a)
soln2 = (-b - d) / (2 * a)
print("The solution is {0} & {1}".format(soln1,soln2))