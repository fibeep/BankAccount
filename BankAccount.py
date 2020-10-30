from random import randint

class BankAccount:
    balance = 0.00
    routing_number = 123456789
    account_number = randint(100000000,999999999)
    """ Initializes Bank Account with Attributes """
    def __innit__(self, full_name):
        self.full_name = full_name
        
    
    """ Adds a deposit function to edit the balance """
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}')
        print(f'New Balance: ${self.balance}')
    
    """ Adds a withdraw function that edits balance """

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Amount Widrawn: ${amount}')
            print(f'New Balance: ${self.balance}')
        else:
            print("You did not have enough funds. You will now be hit with an overdraft fee of $10")
            self.balance -= 10
            print(f'New Balance: ${self.balance}')

    """ Prints a friendly message about balance and returns balance"""

    def get_balance(self):
        print(f"Your Balance is: ${self.balance}")
        return self.balance

    """ Adds interest to users balance """

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest  


salo = BankAccount()
salo.get_balance()
salo.deposit(1000)
salo.add_interest()
salo.get_balance()
salo.withdraw(900)