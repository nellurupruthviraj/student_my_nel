class P:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def abc (self):
        print(f"My name is {self.name}, I am {self.age} years old")

class C(P):
    def __init__ (self,name,age,grade):
        super().__init__(name.age)
        self.grade=grade
    def ab(self):
        super().abc()
        print(f"I am a student in grade {self.grade}")

a=P("Suman",30)
a.abc()
#b=C("nitin",29,9)
#b.ab()


#### Single or Simple Inheritance:
class parent:
    def fun1(self):
        print("Hello Parent")
class child(parent):
    def fun2(self):
        print("Hii child")

test=child()
test.fun1()
test.fun2()

#### Multiple Inheritance:
class parent1:
    def fn1(self):
        print("HElLO Parent:1")

class parent2:
    def fn2(self):
        print("Hii Parent:2")

class parent3:
    def fn3(self):
        print("Whatsup Parent:3")

class child(parent1,parent2,parent3):
    def fn4(self):
        print("HII ALL PARENTS")

test=child()
test.fn1()
test.fn2()
test.fn3()
test.fn4()
print(child.__mro__ )


#### Multilevel Inheritance:
class gp:
    def fn1(self):
        print("HII GP")
class p(gp):
    def fn2(self):
        print("HELLO PARENT")
class C(p):
    def fn3(self):
        print("Hello CHILD")

test=C()
test.fn1()
test.fn2()
test.fn3()

### Hirachical Inheritance:
class parent:
    def fn1(self):
        print("HELLO PARENT")

class child1(parent):
    def fn2(self):
        print("HELLO CHILD 1")

class child2(parent):
    def fn3(self):
        print("HELLO CHILD 2")

class child3(parent):
    def fn4(self):
        print("HELLO CHILD 3")

test=child1()
test2=child2()
test3=child3()
test2.fn1()
test.fn2()
test2.fn3()
test3.fn4()

#### Hybride Inheritance:
class parent1:
    def fn1(self):
        print("HELLO PARENT 1")

class parent2:
    def fn2(self):
        print("HELLO PARENT 2")

class child1(parent1):
    def fn3(self):
        print("HELLO CHILD 1")

class child2(child1,parent2):
    def fn4(self):
        print("Hello CHILD 2")

test=child2()
test.fn1()
test.fn2()
test.fn3()
test.fn4()




