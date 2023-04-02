from bankaccount import BankAccount, InsufficientFundsException
# create two bank accounts
account1 = BankAccount("11111", balance=500)
account2 = BankAccount("33333", balance=1000)

# try to withdraw money from account1
try:
    account1.withdraw(1000)
    print(account1)
except InsufficientFundsException as exception:
    print(exception)
    print(account1)

try:
    account2.withdraw(600)
    print(f"Withdrawal successful Your Account balance is now £{account2.balance}")
except InsufficientFundsException as exception:
    print(exception)

