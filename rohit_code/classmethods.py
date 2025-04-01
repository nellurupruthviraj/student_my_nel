class maths:
    def __init__ (self,a,b):
        self.a = a
        self.b = b
        print(a+b)

    def subtract(self,c):
        print(self.a-self.b+c)  # no need of self to c because it local or same method
add = maths(1,3)
print(add.subtract(4)) # to call a method object.methodname()
