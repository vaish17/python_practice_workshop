f = open("f1.txt",'w')
f.write("welcome to python")
f.write("\ni am vaishnavi")
f.write("\ncse")
f.close()

i = open("f1.txt",'r')
a = i.read()
print a
i.close()

f = open("f1.txt",'r')
d = f.seek(5,0)
g = f.read(2)
e = f.seek(2,1)
b = f.readline(10)
k = f.seek(-4,2)
h = f.read(4)
c = f.tell()
print g
print b
print h
f.close()

