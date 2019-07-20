n=int(input("Enter the number:  "))
a=[]

for i in range(0, n):
    elem=int(input("Enter element :"))

    a.append(elem)

avg=sum(a)/n
print(avg)
