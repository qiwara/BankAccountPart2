from bank import CoolBank

class Checking(CoolBank):

    def __init__(self, customer_name, transfer_limit):
        super().__init__(customer_name)
        self.transfer_limit = transfer_limit

    # avoided using deposit() & withdraw() because they had print statements within that should be in transfer()
    def transfer(self, transfer_amount, other_account):
        if transfer_amount > self.transfer_limit:
            print(f'{self.customer_name}, ${transfer_amount} could not be transferred. Transfer exceeds ${self.transfer_limit}\n')
        elif self.current_balance - transfer_amount < self.minimum_balance:
            print(f'{self.customer_name}, ${transfer_amount} could not be transferred. Account balance insufficient\n')
        else:
            self.current_balance -= transfer_amount
            other_account.current_balance += transfer_amount
            print(f'{self.customer_name}, ${transfer_amount} has been successfully transferred')