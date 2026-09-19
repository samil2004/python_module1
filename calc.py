from module import *

x=int(input("enter the number"))
y=int(input("enter the number"))
opr=input("enter the operator")

if opr=="+":
    print(add(x,y))
    
elif opr=="-":
    print(sub(x,y))

elif opr=="*":
    print(mul(x,y))

else:
    print(div(x,y))
    



