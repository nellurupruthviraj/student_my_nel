import math
a = int(input("enter the number"))
def prime(a):
    b = 0
    if a>10:
        for i in range(2,int(math.sqrt(a))+1):
            if a%i==0:
                b = b+1
                break
    return b

def primenum():
    for i in range(2,a):
        b = prime(i)
        if b<1:
            print(i)
primenum()
