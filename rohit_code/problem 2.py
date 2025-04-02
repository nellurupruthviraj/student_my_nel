a = input(" enter the string ")
def removeDuplicates (s):
	    # code here
	    a = ""
	    for i in s:
	        if i not in a:
	            a = a + i
	    return a
print(removeDuplicates(a))