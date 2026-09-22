##access specifiers
#there are  three methode
#1:- public->self.name
#2:-protected->self._age
#3;-peivate->self.__password

class Detail():
    def __init__(self,name,age,password):
        self.name=name
        self._age=age
        self.__password=password

    def show_password(self):
        return f"show password {self.__password}"

obj=Detail('samil',22,123)
print(obj.name)
print(obj._age)
print(obj.show_password())
        