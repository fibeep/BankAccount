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

salo = BankAccount()
salo.withdraw(3)