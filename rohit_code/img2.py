a = int(input("enter the number"))
def pal(a):
    b = 0
    d  =0
    c = len(str(a))-1
    #print(c)
    while c>-1:
        b = a%10
        #print(b)
        d = d*10 + b
        a = a//10
        c = c-1
    return d


def finpal():
    for i in range(10,a):
        s = pal(i)
        if s == i:
            print(i)
finpal()

