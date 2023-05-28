##Tebatso_Seshayi_40972364
##A python script that calculate the percentage of semester test. The user will be asked if he/she wishes to calculate or not.
##If the user enters a negative mark a message("Error negative mark" must be displayed.And should stop the program whenever
import time

ask_user = int(input("Hi do you want to calculate your mark? Press 0 to cancel .Any numeric number to continue:) ")) ##Asking the user if wishes to cancel or not
while ask_user!=0: ##using the sentinel value to stop the program if the user doesnt want to continue calculating percentage
    semester_test = int(input("Enter your semester mark: "))##asking user to enter his or her semester mark
    test_total = int(input("Was the test total? :"))##asking user to enter the test total
    if semester_test<0: ##using the if the semester_test is less than zero a message must be displayed below
        print("Error negative mark!!")
    else:##if the condition above is false the program will calculate the percentage
        percentage =(semester_test/test_total)*100 ##calculating percentage
        print("Your semester mark percentage is:",percentage,"%") ##printing the percentage
        time.sleep(2) ##using the time module to wait for two seconds and ask the user if he/she wants to calculate the percentage again
        ask_user = int(input("Hi do you want to calculate your mark again? Press 0 to cancel .Any numeric number to continue:) "
