class BankAccount(object):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
           return 'invalid transaction'
        else:
           self.balance -= amount


class MinimumBalanceAccount(BankAccount):  
    def __init__(self, balance):
        self.balance = balance
        super(BankAccount, self).__init__()

