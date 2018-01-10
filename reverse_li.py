li = [1,2,3,4,5,6,7,8]
size = len(li)
for i in range(0,((size/2)-1)):
    temp = li[i]
    li[i] = li[(size/2)-1]
    li[(size/2)-1] = temp
    size -= 1
print li