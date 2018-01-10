a = input("enter a number")
temp = a
res = 0
while(a):
    i = f = 1
    r = a % 10
    while(i <= r):
        f = f * i
        i += 1
    res = res + f
    a = a / 10
if(res == temp):
    print("it is a strong number")
else:
    print("it is a not a strong number")
    
