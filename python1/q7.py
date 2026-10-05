# 7.Write a Python program to take a list of integers and remove all duplicate elements while preserving the original order.
l1=[1,2,3,4,1,2,3]
l2=[]

for num in l1:
    if num not in l2:
        l2.append(num)

print("original list",l1)
print("after removing duplicate element",l2)