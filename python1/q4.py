class Shape:
    
    def draw(self):
        print("drawing a shape")

class Circle(Shape):
    def draw(self):
        print("drawing a circle")

class Rectangle(Circle):
    def draw(self):
        print("drawing a rectagle")

class Triangle(Rectangle):
    def draw(self):
        print("drawing a triangle")

s1=Shape()
c1=Circle()
r1=Rectangle()
t1=Triangle()
s1.draw()
c1.draw()
r1.draw()
t1.draw()      
