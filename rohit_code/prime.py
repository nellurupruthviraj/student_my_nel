import math
a = int(input("enter the number"))
def prime():
    b = 0
    for i in range(2,int(math.sqrt(a))):
        if a%i== 0:
            b = b+1
            print("not a prime")
            break
    if b<1:
        print("prime")
prime()


