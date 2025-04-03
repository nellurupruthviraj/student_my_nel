X= "I didn\'t know about the meeting."
print(X.capitalize())

X= "I didn\'t know about the meeting."
print(X.casefold())

X= "I didn\'t know about the meeting."
A=X.center(50)  ##take space
print(A)

X= "I didn\'t know about the meeting."
print(X.endswith("."))

X= "I didn\'t know about the meeting."
print(X.find("o")) ## find the index number

A="hello good morning"
B="Im Nitin"
X= "{}, {}, I didn\'t know about the meeting."
print(X.format(A,B))

Name="Nitin"
age=27
X={"Name":Name, "age":age}
print("my name is {Name} and i am {age} years old.".format_map(X))


X= "I didn\'t know about the meeting."
print(X.index("n"))   ### find and index are same


X= "I didn\'t know about the meeting."
print(X.isalnum())

X= "hellogoodmorning"
print(X.isalnum())

X="1.1,1.2,1.3,1.4"
print(X.isdecimal())

X="1234567"
print(X.isdigit())

X= "hello good morning"
print(X.isidentifier())

X= "I didn\'t know about the meeting."
print(X.islower())

X= "hello good morning"
print(X.islower())

X="12,2,22"
print(X.isnumeric())
X="122222"
print(X.isnumeric())


X= "I didn\'t know about the meeting."
print(X.isprintable())

X= "I didn\'t know about the meeting. "
print(X.isspace())

X= "I didn\'t know about the meeting. "
print(X.title())

X= "I didn\'t know about the meeting."
print(X.isupper())

X= "I didn\'t know about the meeting. "
print(X.islower())

X= "I didn\'t", " know", "about the", "meeting."
A=" ".join(X)
print(A)


X= "I didn\'t" " know" "about the" "meeting."
print(X.lower())

X= "  I didn\'t know about the meeting.  "
print(X.lstrip())

X= "  I didn\'t know about the meeting.  "
print(X.rstrip())

X= "  I didn\'t know about the meeting.  "
print(X.strip())

X= "I didn\'t know about the meeting."
print(X.partition("e"))

X= "I didn\'t know about the meeting."
print(X.replace("meeting","Business"))

X= "I didn\'t know about the meeting."
print(X.rfind("t"))

X= "I didn\'t know about the meeting."
print(X.rindex("g"))

'''X= "I didn\'t know about the meeting."
print(X.rjust())'''

X= "I didn\'t know about the meeting."
print(X.rpartition("k"))

X= "I didn\'t know about the meeting."
print(X.rsplit(" "))

X= "I didn\'t know about the meeting."
print(X.split(" "))

X= "I didn\'t know about the meeting."
print(X.splitlines())

X= "I didn\'t know about the meeting."
print(X.startswith("I"))

X= "I didn\'t know about the meeting."
print(X.swapcase())

X= "I didn\'t know about the meeting."
print(X.title())

X= "I didn\'t know about the meeting."
print(X.translate(" "))

X= "I didn\'t know about the meeting."
print(X.upper())

X= "I didn\'t know about the meeting."
print(X.zfill(50))