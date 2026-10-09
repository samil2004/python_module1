#15. Write a python program to create a simple calculator using functions.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
opr = input("Enter the operator: ")

def add(n1, n2):
    print("Result:", n1 + n2)

def sub(n1, n2):
    print("Result:", n1 - n2)

def mul(n1, n2):
    print("Result:", n1 * n2)

def div(n1, n2):
    try:
        print("Result:", n1 / n2)
    except ZeroDivisionError:
        print("Cannot divide by zero")

if opr == "+":
    add(n1, n2)

elif opr == "-":
    sub(n1, n2)

elif opr == "*":
    mul(n1, n2)

elif opr == "/":
    div(n1, n2)

else:
    print("Invalid operator")