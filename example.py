n1= int(input("enter marks for subject 1:"))
n2= int(input("enter marks for subject 2:"))
n3= int(input("enter marks for subject 3:"))
n4= int(input("enter marks for subject 4:"))
n5= int(input("enter marks for subject 5:"))

def add(n1,n2,n3,n4,n5):
    total=n1+n2+n3+n4+n5
    average=total/5
    print(f'total mark\n{total}\naverge mark\n{average}')

    

try:
    add(n1,n2,n3,n4,n5)
    
    

except ZeroDivisionError:
    print("inavalid input")

finally:
    print("mark processing completed")
    