import keyword
print(keyword.kwlist)
1 == 1
#print(keyword)

def a_void_function():
    a = 1
    b = 4
    c = a + b
x = a_void_function()
print(x)

for i in range(1,11):
    if i == 5:
        continue
    print(i)


for i in range(1,12):
    if i == 6:
        break
    print(i)