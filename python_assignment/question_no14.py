#14. Write a function is_palindrome(word) that returns True if the word is palindrome. 
word=input("enter the word:")
def is_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False

print(is_palindrome(word))
    