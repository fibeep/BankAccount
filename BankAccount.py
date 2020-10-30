from random import randint

class BankAccount:
    
    """ Initializes Bank Account with Attributes """
    def __init__(self, full_name):
        self.full_name = full_name
        self.balance = 0.00
        self.routing_number = 123456789
        self.account_number = randint(100000000, 999999999)
        self.display_number = ""
        
    
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
            print(f"You did not have enough funds to withdraw ${amount}. You will now be hit with an overdraft fee of $10")
            self.balance -= amount + 10
            print(f'New Balance: ${self.balance}')

    """ Prints a friendly message about balance and returns balance"""

    def get_balance(self):
        print(f"Your Balance is: ${self.balance}")
        return self.balance

    """ Adds interest to users balance """

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest  

    """  Generates a Displayable Acct Number """

    def display_num(self):

        acc_num = range(len(str(self.account_number)))

        for i in acc_num:
            if i <= 4:
                self.display_number += "*"
            else:
                self.display_number += str(self.account_number)[i]

    """ Prints a receipt containing information """

    def print_receipt(self):
        print(self.full_name)
        self.display_num()
        print(f'Account No.: {self.display_number}')
        print(f'Routing No.: {self.routing_number}')
        print(f'Balance: ${self.balance}')



salo = BankAccount("Salomon Cohen")
salo.get_balance()
print("------------------")
salo.deposit(1000)
print("------------------")
salo.add_interest()

salo.get_balance()
print("------------------")
salo.withdraw(900)
print("------------------")
salo.print_receipt()
print("------------------")

starlight = BankAccount("Starlight")
starlight.print_receipt()
print("------------------")
starlight.deposit(15)
print("------------------")
starlight.withdraw(20)
print("------------------")
starlight.print_receipt()
print("------------------")


Joi = BankAccount("Joi is Awesome")
Joi.deposit(10000000)
print("------------------")
Joi.add_interest()
Joi.print_receipt()
print("------------------")
