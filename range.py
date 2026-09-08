#range inbuild
for i in range(10): #start,stop,size ( 0 ,10,1)
    print(i)

for i in range(1,10,2):
    print(i)
    

#list comprehension

lst=[1,2,3,4,5]
result=[i*2 for i in lst]
print(result)

result=[i*2 for i in range(10)]
print(result)


print([i*2 for i in range(1,11)]) # 2 multiplication


# odd or even
print([i for i in range(1,11) if i%2==0]) # even

print([i for i in range(1,11) if i%2!=0]) # odd
