#p - principal
#n - number of times the interest is compondiing
#r - annual nominal interest rate
#t - time period
#a = p * (1 + (r%n)) * pow(nt)

principle = float     #input(float("Enter the principle amount : "))
rate = int            #input(float("Enter the value of rate: "))
time = int             #input(float("Enter the time period: "))
CI = float()

def com_interest(principle, rate, time):
    CI = principle * (pow((1 + rate / 100), time))
    print(CI)

com_interest(500, 3, 3)


