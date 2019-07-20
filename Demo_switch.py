#''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

def square(x):
    return x * x

def cube(x):
    return x * x * x


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Cube")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6):")
#def number1():
 #   return int(input("Enter first number: "))


if choice == '1':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
  #  localNum1=number1()
   # localNum2 = number1()
    print(num1,"+",num2, "=", add(num1,num2))

elif choice == '2':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
    num1 = int(input("Enter first number: "))
    print(num1,"*",num1, "=", square(num1))

elif choice == '6':
    num1 = int(input("Enter first number: "))
    print(num1,"*",num1,"*",num1, "=", cube(num1))

else:
    print("invalid input")