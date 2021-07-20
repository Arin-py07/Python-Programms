Python Program to Check if a Number is Positive, Negative or 0


Source Code: Using if...elif...else

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


Here, we have used the if...elif...else statement. We can do the same thing using nested if statements as follows.
Source Code: Using Nested if

num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
    
    
The output of both programs will be the same.

Output 1

Enter a number: 2
Positive number

Output 2

Enter a number: 0
Zero

A number is positive if it is greater than zero. We check this in the expression of if. If it is False, the number will either be zero or negative. This is also tested in subsequent expression.
