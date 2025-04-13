#a =  int (input(""))
def factorial():
    a = int(input(""))
    b = a
    while a>1:
        b = b*(a-1)
        a = a-1
    print(b)
factorial()

