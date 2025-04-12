a = int(input("enter the number"))
def perfect():
    b = 0
    for i in range(1,a):
        if a%i==0:
            b =b+i
            #print(b)
    if  b == a:
        print("perfect number")
    else:
        print("not a perfect number")
perfect()