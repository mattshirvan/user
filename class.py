class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def balance(self):
        return self.account_balance

guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
puto = User("Puto Madre", "puto@putosrus.com")

guido.deposit(100).deposit(100).deposit(100).withdraw(50)
print(guido.name + "'s balance is $" + str(guido.balance()))

monty.deposit(200).deposit(200).withdraw(50).withdraw(50)
print(monty.name + "'s balance is $" + str(monty.balance()))

puto.deposit(10000).withdraw(200).withdraw(200).withdraw(200)
print(puto.name + "'s balance is $" + str(puto.balance()))