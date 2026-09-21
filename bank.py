# bank.py created by @EpicDinoDar / Parth

class CoolBank:

    bank_title = "Cool Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.current_balance = 0
        self.minimum_balance = 100

    def deposit(self, added_balance):
        self.current_balance += added_balance
        print(f'{self.customer_name}, ${added_balance} has been deposited\n')

    def withdraw(self, removed_balance):
        if self.current_balance - removed_balance < self.minimum_balance:
            print(f'{self.customer_name}, ${removed_balance} could not be withdrawn. Current account balance must be at least ${self.minimum_balance}\n')
        else:
            self.current_balance -= removed_balance
            print(f'{self.customer_name}, ${removed_balance} has been withdrawn\n')

    def print_customer_information(self):
        print(f'Hey {self.customer_name}! Lets take a look at your current balance at {self.bank_title}.')
        print('--------------------------------------------------------')
        print(f'Current Balance: ${self.current_balance}')
        print(f'*** IMPORTANT: Minimum balance can NEVER go under ${self.minimum_balance}! ***')
        print('--------------------------------------------------------')
        print('Thanks for using CoolBank!')
        print('========================================================')

bankacc1 = CoolBank("Parth")
bankacc1.deposit(121)
bankacc1.withdraw(20)
bankacc1.withdraw(10)
bankacc1.print_customer_information()

bankacc2 = CoolBank("Luigi")
bankacc2.deposit(250)
bankacc2.withdraw(2)
bankacc2.withdraw(11)
bankacc2.print_customer_information()