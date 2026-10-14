# def generator_func():
#     yield 10
#     yield 20
#     yield 30

# x=generator_func()
# print(next(x))
# print(next(x))
# print(next(x))
def fun():
    
    for i in range(10):
        if i%2==0:
            print(i)
        yield "stop"

x=fun()
print(next(x))