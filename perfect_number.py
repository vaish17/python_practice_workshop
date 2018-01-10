a = input("enter a number")
res = 0
for i in range(1,((a/2)+1)):
    rem = a % i
    if(rem == 0):
        res = res + i
if(res == a):
    print("it is a perfect number")
else:
    print("it is not a perfect number")
    