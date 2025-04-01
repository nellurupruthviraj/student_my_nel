class maths:
    def __init__(self):
        self.square=4
    def add(self):
        print("add is called")
    def sub(self):
        print('sub is called')
class science(maths):
    def multiply(self):
        print("multiply is called")
    def sub(self):
        print("sub from science is called")
    def add(self):
        super().add()#it is like appending the content from add method in the parent class
        print("add from science is called")

a = science() # object for child class
a.multiply()  #object.methodname()
a.sub()
a.add()
b = maths()
b.add()
b.sub()
print(a.square)
print(b.square)
#b.multiply()  # wrong bcz class maths has no attribute or method "multiply"