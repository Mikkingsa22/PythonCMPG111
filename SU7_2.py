##Tebatso_Seshayi_40972364
##A Python script that prompts the user to enter two numbers and an operator (+, â€, *, /) to perform a mathemaÆŸcal operaÆŸon on those numbers.
##The program is checking for a division by zero error and print an error message if the user aÆ©empts to divide by zero

number_1 = int(input("Enter your first number: ")) ##asking the user to enter first number
number_2 = int(input("Enter your second number: ")) ##asking the user to ennter second number
operator = input("Enter oparator: ")
if operator == '/' and number_2 == 0: ##checking is user is attemping to devide by zero using if statement
               print("Error - Division by zero") ##printing the Error message
elif operator == '*': ##checking if the oparator is *
    maths = number_1*number_2
    print("The calculated result is :" ,maths)
elif operator == '/' : ##checking if the oparator is /
    maths = number_1/number_2 ##perfoming division
    print("The calculated result is :" ,maths)
elif operator == '+': ##checking if the oparator is +
    maths = number_1 + number_2 ##perfoming addtion
    print("The calculated result is :" ,maths)
elif operator == '-': ##checking if the oparator is -
    maths = number_1 - number_2 ##perfoming substraction
    print("The calculated result is :" ,maths)
else:
    print("invalid oparator")
