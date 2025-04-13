a= int(input("enter the number"))
b = int(input())
c = int(input())
def gof():
    if a<b and b>c:
        print("b is greater")
    elif a>b and a>c:
        print("a is greater")
    else:
        print("c is greater")
gof()