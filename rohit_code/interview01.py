
b = ["1","2","3","4","5","6","7","8","9"]
def ste(a,i,j,k):
    ab = a[j+1:k]
    ad = ab*int(i)
    print(ad,end="")
def num():
    a = input("")
    n = 0
    bc = 0
    bd =0
    for i in a:
        if i in b:
            n = i
        if i == "[":
           bc = a.index(i)
        elif i == "]":
            bd  = a.index(i)
            ste(a,n,bc,bd)
            a = a[bd+1:len(a)]
            #print(a)
num()


