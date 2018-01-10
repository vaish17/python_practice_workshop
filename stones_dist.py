a = input("enter dist1")
b = input("enter dist2")
st = input("enter no. of stones")
for i in range(1,(st + 1)):
    print a * (st - i ) + b * (i - 1) ,