class Person:

    def __init__(self,name,age):
        self.__name=name #private
        self.__age=age

#getter:-access
    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)
        
#setter :-update
    def set_name(self,name):
        self.__name=name

    def set_age(self,age):
        self.__age=age



obj=Person("samil",22)
obj.get_name()
obj.get_age()
obj.set_name("sabu")
obj.get_name()
obj.set_age(35)
obj.get_age()
        