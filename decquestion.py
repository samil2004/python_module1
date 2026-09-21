class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'deposited:${amount}')

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f"withdraw:${amount}")
        else:
            print("insufficient amount")

    def check_balance(self):
        print(f"current balance:${self.balance}")
        
account=BankAccount()
account.deposit(2000)
account.check_balance()
account.withdraw(1100)
account.check_balance()
