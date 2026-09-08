#exception handling
n=int(input("enter the number \n"))

try:
    result=10/n
    print(result)

except ZeroDivisionError:
    print("can't divided by zero")

finally:
    print("excecution is completed")