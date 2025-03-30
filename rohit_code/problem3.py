"""Given two strings s1 and s2 consisting of lowercase characters.
The task is to check whether two given strings are an anagram of each other or not.
An anagram of a string is another string that contains the same characters,
only the order of characters can be different. For example, "act" and "tac" are an anagram of each other.
Strings s1 and s2 can only contain lowercase alphabets."""
a = "allergy"
b = "icallerg"
ac = {}
bc = {}
def cou(c,aq):
    c = {}
    for i in aq:
        c[i] = aq.count(i)
    return c
ad = cou(ac,a)
af = cou(bc,b)
#print(ad)
if ad == af:
    print("true")
else:
    print("false")
