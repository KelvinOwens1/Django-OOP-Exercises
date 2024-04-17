class BankAccount:

    default_accountnumber = 1

    def __init__(self, name):
        self.name = name
        self.accountnumber = BankAccount.default_accountnumber
        BankAccount.default_accountnumber += 1
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return "${:,.2f}".format(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("There is not enough money in the account")
        self.balance -= amount