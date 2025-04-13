class abc:
     def __init__(self,a,b):
         self.city=a
         self.state=b
         print(self.city,self.state)

Call=abc("Bangalore","karnataka")

cal=abc("delhi","mumbai")


class Test:
    def __init__(self,a,b):  ##Instance Variable
        self.a=a
        self.b=b
        print(self.a,self.b)

    def m1 (self): ## Instance method
        self.c=self.a+100  ### Modify
        print(self.a,self.c)

    def m2 (self):
         del self.b  ## Delete


t1=Test(10,20)
t2=Test(40,50)
t1.d=400
t2.d=500
print(t1.d,t2.d)
del t2.d
t1.m1()
t2.m2()
#print(self.a, self.b) ## Its Not Work


class employe:
    def __init__(self):
        self.ENo=111
        self.Ename="Suresh"
        self.Salary=50000


e=employe()
print(e.__dict__)



class employe:
    def __init__ (self):
        self.Eno=1122
        self.Ename="Sharan"
        self.salary=40000

e=employe()
print(e.__dict__)

class Test:
    def __init__ (self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)

t=Test()
t.display()
t.c=t.a + t.b
print(t.a,t.b,t.c)



class Test:
    def __init__ (self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1 (self):
        self.e=50
        del self.d

t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)


class Test:
    def __init__ (self):
        self.n1=100
        self.n2=200
        self.n3=300
        self.n4=400

    def method(self):
        self.n5=500
        del self.n4


T=Test()
print(T.__dict__)
T.method()
print(T.__dict__)
del T.n3
print(T.__dict__)

class Test:
    x=10
    def __init__ (self):
        self.y=20

t1=Test()
t2=Test()
print("t1: ", t1.x,t1.y)
print("t2: ", t2.x,t2.y)
Test.x=888
t1.y=999
print("t1: ", t1.x,t1.y)
print("t2: ", t2.x,t2.y )


class Test:
    a=10
    def __init__ (self, a):
        print(self,a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2 (cls):
            print(cls.a)
            print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

class Test:
    a=777
    @classmethod
    def m1(cls):
        cls.a=888
        Test.a=1000
    @staticmethod
    def m2():
        Test.a=999

print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)


class Test:
    a=10
    def m1 (self):
        self.a=800

t1=Test()
t1.m1()
print(Test.a)
print(t1.a)
print(Test.a)


class Test:
    x=100
    def __init__ (self):
        self.y=200

t1=Test()
t2=Test()
print("t1: ",t1.x,t1.y)
print("t2: ",t1.x,t2.y)
t1.x=8888
t2.y=9999
print("t1: ",t1.x,t1.y)
print("t2: ", t2.x,t2.y)

class Test:
    a=10
    def __init__ (self):
        self.b=20

t1=Test()
t2=Test()
Test.a=8888
t1.b=9999
print(t1.a,t1.b)
print(t2.a,t2.b)


class Test:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=1111
        cls.b=2222

t1=Test()
t2=Test()
t1.m1()
Test.b=10000
print(t1.a, t1.b)
print(t2.a,t2.b)
print(Test.a, Test.b)

##Local variable
class Test:
    def M1(self):
        a=1000
        print(a)
    def M2(self):
        b=2000
        print(b)

t=Test()
t.M1()
t.M2()

class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)
        #print(a)

t=Test()
t.m1()
t.m2()




class company:
    def __init__(self):
        self.name="Amezon"
        self.Sdate=1990
        self.Etotal=5000
        self.address="Bangalore"
    def md (self):
        self.distance="50Km"
        del self.Etotal


C=company()
print(C.__dict__)
C.md()
print(C.__dict__)




class total:
    def __init__ (self):
        self.a=100
        self.b=200
        total.c=300
        self.d=400
    @classmethod
    def add (cls):
        cls.e=500
        total.f=600
    @staticmethod
    def add1():
        total.g=700
        total.h=800

T=total()
T.z=T.a+T.d
print(T.z)
total.add()
print(total.e)
total.add1()
print(total.h)













