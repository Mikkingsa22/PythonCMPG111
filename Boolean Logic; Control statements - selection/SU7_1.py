##Tebatso_Seshayi_40972364
##A python script that prompts the user to enter their age and gender (as "M" for male or "F" for female). The program should check whether:age is 18 or above, and gender is "M" or "F".

user_age = int(input("Enter your age: ")) ##Asking the user to enter age
user_gender = str(input("Is your gender M for Male or F for Female?:  ")) #Asking user to enter age as "M" for male or "F" for female
if (user_age>=18) and (user_gender == 'M' or user_gender == 'F'): ##checking wether the user is over 18 and gender is male or female using IF-ELSE statement
    print("You are eligible to vote") ##printing the message when the condition is true
    
elif user_gender != 'M' and user_gender != 'F' : ##setting gender to M and F
    print("Invalid gender")
else:
    print("You are not eligible to vote") ##printing the message when the condition is false
