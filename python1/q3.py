class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Square(Rectangle):
    def __init__(self, length,width):
        super().__init__(length,width)

    def area(self):
        return self.length**2

r1=Rectangle(3,4)
print("area of rectangle:",r1.area())

s1=Square(3,4)
print("area of square:",s1.area())
        
        