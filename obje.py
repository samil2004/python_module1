#encapsulation :- rapping of atribute and methode is known as encapsulation
# class Detail:
    
#     x=10
#     y=20
#     def student_detail(self): #methode
#         print("hello world")

# obj=Detail()       
# obj.student_detail()
# print(obj.x)
# print(obj.y)

# #inheritance

# class Parent:
#     x=10
#     def parent_method(self):
#         print("this is parent")

#     def detail(self):
#         print("this is detail")

# class Child(Parent):
#     x=20
#     def detail(self):
#         print("this is child method")

# obj=Parent()
# obj1=Child() #polymorphism
# obj1.parent_method()
# obj1.detail()

# print(obj1.x)


class Student_detail:

  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department


  def student_detail(self):
    print(f"Student name:{self.name}, Student age:{self.age},Department:{self.department}")


  

obj = Student_detail('Rahul', 22, 'CS')
obj.student_detail()