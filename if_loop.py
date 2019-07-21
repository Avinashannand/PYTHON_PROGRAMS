#a=3
#b=9

#if b % a == 0 :
 #   print "b is divisible by a"
##   print "Increment in b produces 10"
#else:
 #   print "you are in else statment"


#a = 4
#b = 9
#if b % a == 0 :
#    print ("b is divisible by a")
#elif b + 1 == 10:
#    print ("Increment in b produces 10")
#else:
#    print ("You are in else statement")

#function for checking divisibility

def checkDivisibility(a, b) :
    if a % b == 0 :
        print ("a is divisible by b")
    else:
        print ("a is not divisible by b")
checkDivisibility(4, 2)