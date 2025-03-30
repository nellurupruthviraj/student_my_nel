a='''Once upon a time, in the heart of Patna,
lived a little monkey named Mimi who loved to play hide-and-seek with her friends. 
One sunny afternoon, she hid behind a big banyan tree, 
and everyone started searching for her'''
print(str(a))

a='''Once upon a time, in the heart of Patna,
lived a little monkey named Mimi who loved to play hide-and-seek with her friends. 
One sunny afternoon, she hid behind a big banyan tree, 
and everyone started searching for her'''
def my_find():
    if "tree" in a:
        print("yes,'tree' present in a")
    elif "searching" in a:
        print("yes,'searching' Not present in a")

my_find()

a='''Once upon a time, in the heart of Patna,
lived a little monkey named Mimi who loved to play hide-and-seek with her friends. 
One sunny afternoon, she hid behind a big banyan tree, 
and everyone started searching for her'''

print('upon' in a)
print('Patna' not in a)

a="Once upon a time, in the heart of Patna,"
print(a.upper())

A="One sunny Afternoon, She hid behind a big banyan tree,"
print(A)
print(A.lower())

A="  One sunny  afternoon, she   hid behind a   big banyan tree,   "
print(A)
print(A.strip())

a="Once upon a time, in the heart of Patna,"
print(a.replace("upon","in"))

a="Once upon a time, in the heart of Patna,"
print(a.replace("Patna", "Bangalore"))

a='''Once upon a time, in the heart of Patna upon,
lived a little monkey upon named Mimi upon who loved to play hide-and-seek with her friends.'''
s=a.count("upon")
print(a.replace("upon","Day", 3) )

a="Once upon a time, in the heart of Patna upon,"
print(a.split())

a="Once upon a time, in the heart of Patna upon,"
print(a[2:10])
print(a[:10])
print(a[5:])
print(a[ : :2])


a=[10,20,30,40,50,60,70,80,90]
print(a)
print(a[1:5])
a=[2,1,3,5,6,9,7,8]
a.sort()
print(a)
a.reverse()
print(a)