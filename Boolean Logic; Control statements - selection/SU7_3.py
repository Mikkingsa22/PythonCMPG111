##Tebatso_Seshayi_40972364
##A python script that prompts the user to enter a base and an exponent.
##The program is using if statements to check whether the exponent is negaÆŸve
##The program is using or, and, or not operators to check if BOTH the base and exponent are not zero (since 0 to the power of 0 is not defined).
##The program is then to use the pow() funcÆŸon from the math module to perform exponenÆŸaÆŸon of the base to the exponent

import math ##importing the math module

base_number = int(input("Enter your base number: ")) ##asking user to enter the base number
exponent_number = int(input("Enter your exponent: ")) ##asking user to enter the exponent number
if exponent_number<0: #checking if exponent is not negative if negative message must displayed
    print("Error â€“ exponent cannot be negative") ##printing message
elif base_number == 0 and exponent_number == 0: ##Using or, and, or not operators to check if BOTH the base and exponent are not zero (since 0 to the power of 0 is not defined)
    print("Error â€“ indefinite form (0Ë„0)") ##printing message
else:
    exponentiation = pow(base_number, exponent_number) ##Using the pow() funcÆŸon from the math module to perform exponentiation of the base to the exponent if the privious condition is not true
    print("The calculatated result is: " ,exponentiation) ##printing message and results from the pow() function
