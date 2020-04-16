class BankAccount():
    def __init__(self, interest, balance):
        self.interest = interest 
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.account_balance:
            self.account_balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self
        else:
            self.account_balance -= amount
            return self
    def balance(self):
        return self.account_balance
    def rate(self):
        if self.account_balance > 0:
            self.account_balance * self.interest
            return self

