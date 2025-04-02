"""
You are given a string, 'S'. You need to write a function called 'gfg' that takes 'S' as input
and checks if the string starts and ends with the substring 'gfg'.
"""
a = input("enter the string releated  to this question")
def gfg(S):
    b = S.lower()
    if b.startswith("gfg") and b.endswith("gfg"):
        print ("Yes")
    else:
        print ("No")
gfg(a)