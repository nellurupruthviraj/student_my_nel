# To Create a set
set1 = {2,6,56,4454,3,1,3,4}  # or variable = set(values)
set2 = {22,"sai","Suhhhvu","rohuthi",5,5,9,5,6,}
print(set1)
print(set2)
# sets don't print duplicate values
# sets are unordered
# in sets indexing is not allowed ,slicing is not allowed
set3 = {True,0,1,False} # this will print [1 or True] and [0 or False]
print(set3)
set4 = {} #this is not an empty set ,, it is dictionary
set5 = set() #this is empty set
print(type(set4))
print(type(set5))
#methosds
set1.clear()
print(set1)
print(set2.pop())
print(set2)
set2.add((6265,56464)) #we can add tuple to  a set but not list to a set
set2.add(2165) # bcz tuples are immutable, lists are mutuable
print(set2)