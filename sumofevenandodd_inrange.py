srange = input("enter start of range")
erange = input("enter end of range")
sumeven = 0
sumodd = 0
i = srange
while(i <= erange):
    if(i % 2 == 0):
        sumeven = sumeven + i
    else:
        sumodd = sumodd + i
    i += 1
print("sum of even digits is",sumeven)
print("sum of odd digits is",sumodd)