from bank_account import BankAccount

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(0.02, 0)

    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def balance(self):
        return self.account.balance()

guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
puto = User("Puto Madre", "puto@putosrus.com")

guido.deposit(100).deposit(100).deposit(100).withdraw(50)
print(guido.name + "'s balance is $" + str(guido.balance()))

monty.deposit(200).deposit(200).withdraw(50).withdraw(50)
print(monty.name + "'s balance is $" + str(monty.balance()))

puto.deposit(10000).withdraw(200).withdraw(200).withdraw(200)
print(puto.name + "'s balance is $" + str(puto.balance()))