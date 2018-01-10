first = input("enter first number")
second = input("enter second number")
num = input("enter the range")
print first
print second
for i in range(2,num):
    temp = first + second
    print temp
    first = second
    second = temp
    
