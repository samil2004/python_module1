# recursion= a fumction calling itself
def x(i):
    print("recursion")

    if i==10:
        return
    else:
        x(i+1)  


x(1)