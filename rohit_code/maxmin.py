#a = int(input("enter the number"))
def maxmin():
    a = int(input("enter the number"))
    b = 0
    d = 0
    e =0
    g =45547946524325
    while a>0:
        b = a%10
        bc = b
        a = a//10
        if b>=d:
            d = b
        if g>b :
            #print(d)
            e = b
        #print(d)
    print(f"{e} is the min digit")
    print(f"{d} is the max digit")
maxmin()
