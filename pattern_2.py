a = input("enter the number")
b = a 
for i  in range(1,(a+1)):
    b -= 1
    for i in range(1,(b+1)):
        print "+", 
    for i in range(0,(a-b)):    
        print "*",
    print ""

