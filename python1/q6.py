# 8.Write a Python program that checks whether a given string is a palindrome  or not.

str=input("enter the string")

if str==str[::-1]:
    print(str,"is palindrom")

else:
    print(str,"is not a palindrom")