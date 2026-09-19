def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    
    try:
        return x/y
    
    except ZeroDivisionError:
        print("inavalid")
        
    finally:
        print("program is completed")
        

def mul(x,y):
    return x*y




