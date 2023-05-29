##Tebatso_Seshayi_40972364

import math
print("Cuboid calculator")

base_number = int(input("Enter the base (cm): ")) ##asking the base number of triangular prism
length_cm = int(input("Enter the Length (cm): ")) ##asking the length number of triangular prism
height_cm = int(input("Enter the Height (cm): ")) ##asking the height number of triangular prism
area = base_number*length_cm + length_cm*height_cm + base_number*height_cm + height_cm*math.sqrt(length_cm*length_cm + base_number*base_number) ##Entering the formula to calculate the area of triangular prism
volume = (length_cm*base_number*height_cm)/2  ##Entering the formula to calculate the volume of triangular prism
space_d = math.sqrt(length_cm*length_cm + base_number*base_number + height_cm*height_cm) ##Entering the formula to calculate the space diagonal of triangular prism
print("Area of the triangular prism is " , round(area, 4), "square cm" ) ##displaying area rounded of to the nearest 4
print("Space diagonal of the triangular prism is " , round(space_d, 3),"cm" )  ##displaying area rounded of to the nearest 3
print("Volume of the triangular prism is " , round(volume, 2), "cubic cm") ##displaying area rounded of to the nearest 2

print("**Triangular prism dimensions:**")
print("base =",round(base_number,1), "cm" , "length =" , round(length_cm, 1) , "cm" , " height = ", round(height_cm, 1) ,"cm") ##displaying dimesions of traingular prism float
