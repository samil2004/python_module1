#6. Write a program to generate the first n Fibonacci numbers and print their sum. 
n=int(input("enter the number"))
a=0
b=1
sum=0
for i in range(n):
    print(a)
    sum=sum+a
    a,b=b,a+b
    

print(f"sum of {n} fibonaaci number",sum)