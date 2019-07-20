#num1 = int(input("Enter the number: "))

#def factorial():
    #num1 * num1

#for i in range(1, num1):
#    num1 = num1 * i
#    num1 += num1
#    print("Factorial is ",num1)

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = int(input("Enter the number: "))

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)