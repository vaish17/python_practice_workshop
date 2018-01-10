li = [1,6,3,5,8,2,7,4]
#print li
size = len(li)
a = 0
for i in range(0,(size)):
    for j in range(size,0):
        if((li[j] % 2) == 0):
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
            i += 1
        j -= 1
print li


    
        

