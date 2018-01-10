a = raw_input("enter a number")
count = len(a)
temp = 0
i = 1
while(count > i):
    if(a[i-1] > a[i]):
        print "false"
        temp = 1
        break
    i += 1
if(temp != 1):
    print "true"
   
