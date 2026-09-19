n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
opr=input("enter the operator:")

def add(n1,n2):
    result=n1+n2
    print(result)

def sub(n1,n2):
    result=n1-n2
    print(result)

def mul(n1,n2):
    result=n1*n2
    print(result)

def div(n1,n2):
    result=n1/n2
    print(result)

if opr=="+":
    add(n1,n2)
    
elif opr=="-":
    sub(n1,n2)

elif opr=="*":
    mul(n1,n2)

else:
    div(n1,n2)