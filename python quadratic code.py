from math import *
a = float(input('Enter the value of "a" to solve for x: '))
b = float(input('Enter the value of "b" to solve for x: '))
c = float(input('Enter the value of "c" to solve for x: '))
d = b**2 - 4*a*c           
D = d**0.5
X1 = (-b + D)/(2*a)
X2 = (-b - D)/(2*a)

print("The values of x are {0}, and {1}".format(X1,X2))



if d <= 0 : print("The eqution has real and unequal roots")
elif d == 0 : print("The eqution has real and equal roots")
elif d >= 0 : print("The eqution has imaginary roots")
else : print("Invalide Input") 






 
 
