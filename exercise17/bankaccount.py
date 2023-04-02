class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Account number: {self.account_number}, Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundsException("Unable to complete transaction: Insufficient funds")
        self.balance -= amount
