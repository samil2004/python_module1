# Function to check whether a number is odd or even
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")
    except ValueError:
        print("Please enter a valid integer.")
