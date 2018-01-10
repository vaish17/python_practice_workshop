class parent:
    def add(self,x,y):
        return x + y
class child(parent):
    def sub(self,x,y):
        return x - y
    def init(self,x):
        print x
o = child()
print o.add(6,5)
print o.sub(9,3)
o.init("vaishnavi")
