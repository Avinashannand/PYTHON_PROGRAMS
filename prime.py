#n = int
#i = int
#flag = int
#def prime(n,i,flag):
 #   """This will give the result
  #      that number is prime or not"""
   # for i in n:
    #    if (n%i == 0):
     #       flag = 1
      #  break

num1 = int(input("Enter the numer: "))

#if(flag == 0):
 #       print("Number is prime", num1)
#else:
 #       print("Number is not prime, num1")


if num1 > 1:
    for i in range(2, num1):
        if (num1%2 == 0):
            print(num1, "is not a prime number")
            #print(i, "times", num1 // i, "is", num1)
            break
        else:
            print(num1, "is a prime number")

        # if input number is less than
        # or equal to 1, it is not prime
        #else:
           # print(num1, "is not a prime number")
