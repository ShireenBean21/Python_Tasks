class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsException("Unable to complete transaction: Insufficient Funds")


        return f"{type(self).__name__}({self.acc_no}, {self.balance})
