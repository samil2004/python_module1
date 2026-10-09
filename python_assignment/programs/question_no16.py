#16. Write a function check_even_odd(num) that takes a number and prints whether its even or odd. 
num=int(input("enter the number"))
def check_even_odd(num):
    if num%2==0:
        print(num,"is even number")

    else:
        print(num,"is odd number")

check_even_odd(num)