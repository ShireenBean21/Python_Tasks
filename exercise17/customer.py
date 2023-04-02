from bankaccount import BankAccount
from bankaccount import InsufficientFundsException

account1 = BankAccount("11111", balance=500)
account2 = BankAccount("33333", balance=1000)

try:
    account1.withdraw(1000)
    print(account1)
except InsufficientFundsException as exception:
    print(exception)
    print(account1)

print(account2)
