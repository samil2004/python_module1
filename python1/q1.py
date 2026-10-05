class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self, name, age,salary):
        
        super().__init__(name, age)
        self.salary=salary


obj=Employee("samil",22,12000)
print(obj.name)
print(obj.age)
print(obj.salary)