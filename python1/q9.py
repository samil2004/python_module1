# Write a Python progran to calculate sum of the first 10 prime numbers without using inbuilt methods ?
count=0
sum=0
num=2
        
while count<10:
    is_prime=True
    

    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

    if is_prime:
        print(num)
        sum=sum+num
        count+=1
        
    num=num+1

print("Sum of first 10 prime numbers:", sum)