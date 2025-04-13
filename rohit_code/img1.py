a = input("enter the string")
def pal():
    b = ""
    for i in range(1,len(a)+1):
        b = b +a[-i]
    if a == b:
        print("palindrome")
    else:
        print('not a palindrome')
pal()
