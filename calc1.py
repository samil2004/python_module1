x=int(input("enter the number\n"))
y=int(input("enter the number\n"))
opr=input("enter the operator\n")
class Calculator:

    def add(self,x,y):
        return x+y

    def sub(self,x,y):
        return x-y

    def mul(self,x,y):
        return x*y

    def div(self,x,y):
        try:
            return x/y
        except ZeroDivisionError:
            print("invalid")
        finally:
            print("program is completed")

obj=Calculator()
if opr=="+":
    print(obj.add(x,y))

elif opr=="-":
    print(obj.sub(x,y))

elif opr=="*":
    print(obj.mul(x,y))

else:
    print(obj.div(x,y))