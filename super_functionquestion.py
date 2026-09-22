class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
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

    def interest(self):
        result=self.balance*0.02
        return result



class SavingAccount(BankAccount):


    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    # def deposit(self,amount):
    #     self.balance=self.balance+amount
    #     print(f'deposited:${amount}')

    # def withdraw(self,amount):
    #     if amount<=self.balance:
    #         self.balance=self.balance-amount
    #         print(f"withdraw:${amount}")
    #     else:
    #         print("insufficient amount")

    # def check_balance(self):
    #     print(f"current balance:${self.balance}")

    def interest(self):
        result=self.balance*0.03
        return result   
    def __private_account(self):
        print( "account detail")
        

    


account=BankAccount('samil',2000)
account.deposit(2000)
account.check_balance()
account.withdraw(1100)
print(account.interest())
account.check_balance()

account1=SavingAccount('sabu',3000)
account1.deposit(2000)
account1.check_balance()
account1.withdraw(1100)
print(account1.interest())
account1.check_balance()
account1._SavingAccount__private_account()
