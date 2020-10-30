from random import randint

class BankAccount:
    balance = 0.00
    routing_number = 123456789
    account_number = randint(100000000,999999999)
    """ Initializes Bank Account with Attributes """
    def __innit__(self, full_name, account_number):
        self.full_name = full_name
        
    
    """ Adds a deposit function to edit the balance """
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}')
        print(f'New Balance: ${self.balance}')

salo = BankAccount()
salo.deposit(3)
print(salo.balance)