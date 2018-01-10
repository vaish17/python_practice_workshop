a = input("enter a number")
res = 0
temp = 0
for i in range(1,((a/2) + 1)):
    rem = a % i
    if(rem == 0):
        res = res + i
for i in range(1,((res/2) + 1)):
    rem2 = res % i
    if(rem2 == 0):
        temp = temp + i
if(temp == a):
    print("it is an ambicable number")
else:
    print("it is not an ambicable number")
