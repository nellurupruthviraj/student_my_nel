a = {'key':13,'def':123}
b = {'deft':1235,'def':13443}
 #dict  are ordered and key are immutable and values are mutuable
#dict cannot contain duplicate keys
print(a["def"])
print(b)
a['def'] = 123456 # for changing the value to the key
a['dekk'] = 1232 # for appending key and value.
print(a)
del b['def']
print(b)
print(b.pop('deft'))
print(a.keys())
print(a.values())
print(a.items())
for i in a:
    print(i) # only prints the keys
    print(a[i]) # for values
for i in a.items():
    print(i) # prints key value due to items
c = a.copy()
print(c )