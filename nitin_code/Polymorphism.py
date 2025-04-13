class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages + other.pages

b1=book(10)
b2=book(20)

print(b1+b2)