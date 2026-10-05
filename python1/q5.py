# 5.Create an abstract class Payment with abstract methods make_payment() and payment_status(). Implement two concrete classes CreditCardPayment and UPIPayment. Write a program where the user chooses the payment method and the respective class handles the process.


from abc import ABC,abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def make_payment(self):
        pass
    @abstractmethod
    def payment_status(self):
        pass


class CreditCardPayment(Payment):

    def make_payment(self, amount):
        print(f"{amount} is paid using credit card")

    def payment_status(self):
        print("Credit card payment is successful")


class UPIPayment(Payment):


    def make_payment(self,amount):
            print(f"{amount} is paid using upi")
    
    def payment_status(self):
        print("UPI payment is successful")


amount=float(input("enter the amount"))
    

print("\nChoose payment method:")
print("1. Credit Card")
print("2. UPI")

choice=input("enter the choice")

if choice=="1":
    Payment=CreditCardPayment()

elif choice=="2":
    Payment=UPIPayment()

else:
    print("invalid")


Payment.make_payment(amount)
Payment.payment_status()
