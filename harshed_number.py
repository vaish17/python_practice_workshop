a = input("enter a number")
temp = a
res = 0 
while(temp > 0):
    res = res + (temp % 10)
    temp = temp / 10
if(a % res == 0):
    print ("it is a harshed number")
else:
    print("it is a not harshed number")
