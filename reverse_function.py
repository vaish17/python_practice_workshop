def revs(numb):
    res = 0
    while(numb > 0):
        res = (res * 10) + (numb % 10)
        numb = numb / 10
    return res
val1 = input("enter the first number")
val2 = input("enter the second number")
sum1 = val1 + val2
rval1 = revs(val1)
rval2 = revs(val2)
sum2 = rval1 + rval2
temp = revs(sum2)
if(temp == sum1):
    print("it is strictly reverse")
else:
    print("it is not strictly reverse")
