#17. Write a function reverse_number(n) that returns the reverse of a number. 
n=int(input("enter the number"))

def reverse_number(n):
    result=0
    while(n>0):
        digit=n%10
        result=result*10+digit
        n=n//10
    print("reverse number:",result)
reverse_number(n)

    