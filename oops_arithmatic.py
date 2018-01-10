class operation:
    def add(self,x,y):
        return x + y
    def sub(self,x,y):
        return x - y
    def mul(self,x,y):
        return x * y
    def div(self,x,y):
        return x / y
    def rem(self,x,y):
        return x % y
    def pow(self,x,y):
        return x**y
    def flrdiv(self,x,y):
        return x//y
o = operation()
print o.add(6,3)
print o.sub(7,3)
print o.mul(2,4)
print o.div(10.0,3)    
print o.rem(45,10)
print o.pow(2,2)
print o.flrdiv(4,3)