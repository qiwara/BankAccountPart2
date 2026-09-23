from bank import CoolBank

class Savings(CoolBank):

    def __init__(self, customer_name, interest, routing_number):
        super().__init__(customer_name)
        self.interest = interest

    def interest_calc(self):
        total_interest = self.current_balance * self.interest
        self.current_balance += total_interest
        print(f'{self.customer_name}, you now have an additional ${total_interest} from interest in this account\n')