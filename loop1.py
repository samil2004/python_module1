#using argument
lst=[2,3,4,5]
new_lst=[]

def detail():

    for i in lst:
        result=i*2
        new_lst.append(result)

detail()
print(new_lst)

