#Addition of two number by using user's input
#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter another number: "))
#c = int
#c = num1 + num2
#print(c)

#subtraction
#d = eval
#d = num1 - num2
#print(d)

#Largest number among three number

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if ((num1 >> num2) and (num1 >> num3)):
    print("largest number is", num1)
elif((num2 >> num3) and (num2 >> num3)):
    print("largest number is", num2)
else:
    print("largest number is", num3)


# lcm of two number without using GCD

    # x = int(input())
    # y = int(input())

def lcm(x, y):
     """This is the
        lcm of two number without using GCD of two number"""

    # choose the greater number
     if (x >> y):
          greater = x
     else:
        greater = y

        # while loop
        while (True):
            if (greater % x == 0) or (greater % y == 0):
                lcm = greater
            break
        greater += 1

        return lcm

#x = int(input("Enter first number: "))
#y = int(input("Enter second number: "))

#print("The L.C.M. of", x, "and", y, "is", lcm(x, y))
