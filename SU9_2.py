##Tebatso_Seshayi_40972364
##MULTIPLICATION TABLE
i=0 ##initialising the "i"
summ =0
num=int(input("Enter the number you want it's multiplication to be displayed: ")) ##asking user to enter the number he/she wants to display the multiplication
while num>0: ##input validation by using a while loop
    print("Multiplication of ",num)
    for i in range(1, 13):##providing a multiplication table (from 1 to 12) for the value entered by the user,utilising a for loop.
       multi=i*num ##calculating the product
       print(i, 'x', num, '=', num*i)
       summ += multi##calculating the sum of all numbers
    print("The sum of the number is", summ)##displaying the sum of all numbers
