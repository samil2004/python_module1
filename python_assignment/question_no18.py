#18. Write a program using try, except, else and finally together. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")


else:
    print("Result:", result)

finally:
    print("Program execution completed")