from abc import ABC , abstractmethod
class maths(ABC):
    def __init__ (self,a):
        self.a=a
        #self.b = b
    @abstractmethod
    def add(self):
        pass
class Science(maths):
    def __init__(self,c,d):
        super().__init__("Science")
        self.c = c
        self.d = d
        a=c+d
    def add(self):
        print(f"{a} Add is called from science")
class phy(maths):
    def __init__(self, e):
        super().__init__("phy")
    def add(self):
        print("add from phy")
    def sub(self):
        print("snbkjs")

sci = Science(1,3)
print(sci.add())

