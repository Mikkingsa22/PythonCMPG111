##Tebatso_Seshayi_40972364
##A python program that calculates the two roots of a quadraÆŸc equaÆŸon (x1 and x2),
##this program will ask a user to Ask the user to supply the coefficients (a, b, and c) of a quadraÆŸc equaÆŸon to calculate x1 and x2

import math
print("Solving ax^2 + bx + c = 0")
a = float(input("Enter the value of a : ")) ##input for the velue of a as float
b = float(input("Enter the value of b : "))##input for the velue of b as float
c = float(input("Enter the value of c : "))##input for the velue of c as float

x1 = (-(b)+math.sqrt(b*b - 4*a*c))/2*a  ##the 1st quadratic formula
x2 = (-(b)- math.sqrt(b*b - 4*a*c))/2*a ##the 2nd  quadratic formula

print("ROOTS OF GIVEN QUADRATIC EQUATIONS ARE:")
print("x1: ", x1) #desplaying the roots of the 1st quadratic eqeation            
print("x2: ", x2) ##desplaying the roots of the 1st quadratic eqeation
