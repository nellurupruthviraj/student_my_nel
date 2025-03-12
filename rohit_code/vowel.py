a = input("")
b = ['a',"e","i","o","u"]
print(type(a))
for i in a:
    if i in b:
        print(f"{i} vowel")
    else:
        print(f"{i} consonant")