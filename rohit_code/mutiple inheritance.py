class maths:
    def add(self):
        print("add from maths")
class science:
    def multiply(self):
        print("multiply from science")
class tenth(maths,science):
# order 1    2     3
    def add(self):
        print("add from tenth")
a = tenth()
a.add()
# it prints from tenth class but u want from maths class then
maths.add(a)  # it will print from maths class
# classname.method(object)
a.multiply()
# to know the order of class how it is taking we use mro
print(tenth.mro())
# method resolution order