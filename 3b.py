import cmath
#use eval for inputing complex no
num = eval(input("Enter the complex no: "))
num_sqrt = cmath.sqrt(num)
print("The Square root of {0} is {1:0.3f} + {2: 0.3f}j".format(num,num_sqrt.real,num_sqrt.imag))