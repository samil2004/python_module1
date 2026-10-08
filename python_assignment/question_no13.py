#13. Write a function is_prime (n) that checks whether a number is prime or not.
n=int(input("enter the number"))
def prime(n):
    
    if n < 2:
        print(n, "is not a prime number")
        return
    for i in range(2,n):
        if n%i==0:
            print(n,"is not prime number")
            break
    else:
        print(n,"is prime number")

prime(n)