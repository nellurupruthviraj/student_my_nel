a =  int(input("enter where to stop the series"))
b = int(input("enter the ratio"))
def gp():
    c= 1
    while  c<=a:
        c= c*b
        if c<=a:
            print(f" {c}",end = "")
        else:
            break
gp()

