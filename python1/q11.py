# Q1. Build a base class Product with attributes name and price. Derive Electronics and Clothing classes that add warranty and size respectively. Override the display() method to include these details.
# Q2. Extend the system by adding a new class Furniture (inheriting from Product) with an attribute material, and override the display method.
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price


    def display(self):
        print("product name:",self.name)
        print("product price:",self.price)
        
        

class Electronics(Product):
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty=warranty
        
    def display(self):
        super().display()
        print("product warranty:",self.warranty)
        
     
    
        
class Clothing(Electronics):
    def __init__(self, name, price, warranty, size):
        super().__init__(name, price, warranty)
        self.size=size

    def display(self):
        super().display()
        print("product size:",self.size)


class Furniture(Product):
    def __init__(self,name,price,material):
        super().__init__(name,price)
        self.material=material

    def display(self):
        super().display()
        print("product material:",self.material)
        

v1=Product("NIKE",2000)
v1.display()
print()

v2=Electronics("laptop",20000,"1 year",)
v2.display()
print()

v3=Clothing("addidas shirt",1000,"6 month","s")
v3.display()
print()

v4=Furniture("sofa",2000,"leather")
v4.display()