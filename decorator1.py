# decorators:- a decorator is essentially a function that takes anotherfunction as an argument and return anew function with enhanced functionality

def my_decorator(funct):
    def wrapper():
        funct()
        print("this is dectorator function")
    return wrapper


@my_decorator
def greet():
    pass
greet()