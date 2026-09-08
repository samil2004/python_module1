x=10 #global variable
def detail():
    print(x)

detail()
print(x)

#local variable using access in funtion
x=10
def detail():
    y=20
    print(x)
    print(y)

detail()
print(x)
