class Detail():

    def __init__(self,length):
        
        self.length=length

    def area_square(self):
        result=self.length*self.length
        return f"area of square {result}"

    def parimeter_square(self):
        result1=4*self.length
        return f"area of parimeter {result1}"


obj=Detail(5)
print(obj.area_square())
print(obj.parimeter_square())