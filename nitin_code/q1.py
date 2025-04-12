b = ["1","2","3","4","5","6","7","8","9"]
def se(j,k):
    ad = j*int(k)
    print(ad,end="")
def sd():
    a = input("enter")
    c = 0
    d = 0
    e = 0
    for i in a:
        if i in b:
            c = i
        if i =="[":
           d = a.index(i)
           #print(d)
        if i == "]":
            e = a.index(i)
            f = a[d+1:e]
            #print(e)
            se(f,c)
            a = a[e+1:len(a)]
sd()