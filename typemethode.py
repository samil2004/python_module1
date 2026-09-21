class Student():
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1

    #instance methode
    def detail(self):
        print(f"my name is {self.name}")

    #classmethod
    @classmethod
    def class_method(cls):
        print(f'student count:{cls.count}')

    #staticmethod
    @staticmethod
    def static_method(a,b):
        return a+b



obj=Student('samil')
obj.detail()
obj1=Student('sabu')
obj1.detail()
Student.class_method()
print(Student.static_method(10,8))
