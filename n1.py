# x = [1, 2, 3]
# y = x 
# z = x.copy() 
# y.append(4) 
# z.append(5) 
# print(x, y, z)

# funcs = []
# for i in range(5): 
#     funcs.append(lambda i=i:i) 
# print([f() for f in funcs])


# def add_item(item, items=[]): 
#     items.append(item) 
#     return items 
# print(add_item(1)) 
# print(add_item(2)) 
# print(add_item(3, [])) 
# print(add_item(4))

# a = 10 
# b = 20 
# a, b = b, a + b 
# print(a, b)

# a = 256
# b = 256 
# c = 345
# d = 345
# print(a is b) 
# print(c is d) 
# print(a == b, c == d)

# class A:
#  x = 10 
# class B(A):
#     x = 20 

# a = A() 
# b = B() 
# print(a.x, b.x) 
# A.x = 30 
# print(a.x, b.x)

# def outer():
#  x = 10 
#  def inner():
#    nonlocal x 
#    x += 5
#    return x 
#  return inner 
# f = outer() 
# print(f()) 
# print(f())


# try:
#  print(10 / 0) 
# except ZeroDivisionError: 
#  print("zero") 
# else: 
#     print("else") 
# finally: 
#   print("finally")

# def f():
#  print("A") 
#  yield 1 
#  print("B") 
#  yield 2 
# g = f() 
# print(next(g)) 
# print(next(g))




# def log(number):
#     nums=set(number)
#     longest=0

#     for num in nums:
#         if num-1 not in nums:
#             lenght=1

#         while num + lenght in nums:
#             lenght+=1

#         longest=max(longest,lenght)

#     return longest
# print(log([100, 4, 200, 1, 3, 2]))




# def prime_numbers():
#     num = 2

#     while True:
#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             yield num

#         num += 1


# g = prime_numbers()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#kwargs :-keyword arguments
def detail(**kwargs):
    print(f'my name is {kwargs['name']}, Iam age is {kwargs['age']},my department is {kwargs['department']}')
    
detail(name="samil",age=22,department="cs")

##*args       → positional values → tuple
##**kwargs    → keyword values    → dictionary

def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(10, 20, name="Samil", age=22)