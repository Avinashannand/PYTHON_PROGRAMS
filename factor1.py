num1 = int(input("Enter the number: "))

def factor_of_number(x):

    print("The factor of number :")
    for i in range(1, num1+1):
        if x % i == 0:
            print(i)

print(factor_of_number(num1))