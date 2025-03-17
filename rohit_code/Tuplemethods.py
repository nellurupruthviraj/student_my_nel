tuple1 =(10,39,3980,890)
tuple2 = ("daf" , "viuau","ah")
tuple3 = ("svsv","ewgw","svvs",9,99,9880)
#above are examples of tuple
#exception case
tuple4 = (10) #it is not a tuple
tuple5 = (10,)  #it is tuple because in single element we have to put (,) comma .
a = tuple1[3] #we use square brackets for subscript
b = tuple1[1:3] #slicing
tuple1 = tuple1 + (9,)
print(tuple1)
print(a)
print(b)
print(type(tuple5))
#tuples are immutable you cannot add, remove once it is created and lists are mutable
print(type(tuple4))
#we cannot change the tuple
#tuple3[3 ] =  333
#ruple3 = tuple3.append(34344)
#print(ruple3)  the above arenot suitable in tuple
t = (10,34) * 4
print(t)
#converting list to tuple
l = [ 34,46,76,8778,7,7777,666,7867,]
sr = tuple(l)
ss = list(sr)
sd = set(l)
print(sr)
print(ss)
print(sd)