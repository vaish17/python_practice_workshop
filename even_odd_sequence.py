li = [1,6,3,5,8,2,7,4]
#print li
size = len(li)
a = 0
for i in range(0,(size)):
    if((li[i] % 2) == 0):
        a = li[i]
        li.remove(li[i])
        li.insert(0,a)
print li


    
        

