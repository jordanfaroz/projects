class Account(object):
    def __init__(self, name, initial_amount):
        self.name = name
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def dump(self):
        s = (self.name, self.balance)
        print(s)








