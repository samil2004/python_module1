# arg using number argument passing through the parameter

def add(*arg):
    result=sum(arg)
    print(result)
    
add(2,3,4,5,6)

#argument
def add(x,y):
    result=sum([x,y]) # sum is inbuild function using parameter in list
    print(result)
    
add(2,3)

