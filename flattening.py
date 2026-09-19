#flattening

lst=[[1,2,3,4,5]]
new_lst=[]
for i in lst:
    for j in i:
        new_lst.append(j)

print(new_lst)

#list comprehension using flattening
lst=[[1,2,3,4,5]]

result=[j for i in lst for j in i]
print(result)


print([j*2 for i in lst for j in i])




