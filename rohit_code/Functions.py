"""
def add (a,b): # function  definition and a and b are parameters
    c = a + b
    print(f"{c} is sum of {a} and {b}")
add(1,64) # function calling 1,64 are arguments
add(-55,-554)

"""
"""
def add (* args):  # by using args we can send any no of arguments
    c = 0
    for i in args:
        c = c+i
    print(c)
add(1,2,3,5,4)
add(1)
add(1,2,5,7,8,9,4,2,3)
"""
"""
def  person(**kwargs):
    for i in kwargs.items():
        print(i , end ="")
    print("\n")
    print(kwargs["a"])

person(a = "james"  , b = "cam" , c = "eron" )
person(a = "james" , c = "cameron")

#(*args,**kwargs) # should be like this
# args first and then kwargs

"""
def add(a,b):
    return a+b , a-b # returning multiple values
print(add(1,2))
z = add(22,55)
print(z)