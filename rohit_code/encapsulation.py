class  person:
    def __init__(self,name,age,gen):
        self.__name = name
        self.__age = age
        self.gen = gen

    def get_name(self):
        #return self.__name
        #return self.gen
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age>self.__age:
            self.__age= age
        else:
            return ("ssssssd")
obj = person("rohith",24,"male")
print(obj.get_name())
obj.set_age(25)
print(obj.get_age())
print()