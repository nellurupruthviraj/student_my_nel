class student:
    def name(self):
        print("name from student")
class boys(student):
    def name(self):
        super().name()
        print("name from boys")
class girls:
    def name(self):
        print("name from girls")
fin = [student(),boys(),girls()] #one obj for several classes
for i in fin:
    i.name() #obj.methodname for calling