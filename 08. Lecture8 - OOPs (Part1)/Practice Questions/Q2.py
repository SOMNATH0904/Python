# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:

    def __init__(self, balance, accountNo):
        self.balance = balance
        self.accountNo = accountNo

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Total Balance :", self.getBalance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total Balance :", self.getBalance())

    def getBalance(self):
        return self.balance


acc1 = Account(10000, 12345)
print("Account's Balance is :",acc1.balance)
print("Account number is :",acc1.accountNo)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(65000)
acc1.debit(20000)