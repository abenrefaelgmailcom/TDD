class BankAccount:

    def __init__(self):
        # initialize balance to zero
        self.balance = 0

    def deposit(self, amount):
        # add amount to balance
        self.balance += amount

    def withdraw(self, amount):
        # subtract amount from balance
        self.balance += amount

    def get_balance(self):
        # return current balance
        return self.balance

    def is_empty(self):
        # check if balance is zero
        return self.balance == 0