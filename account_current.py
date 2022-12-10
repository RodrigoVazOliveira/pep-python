class CurrentAccount:
    total_accounts_createds = 0
    tax_operation = None

    def __init__(self, client, agency, number):
        self.balance = 100
        self.client = client
        self.agency = agency
        self.number = number
        CurrentAccount.tax_operation = 30 / CurrentAccount.total_accounts_createds
        CurrentAccount.total_accounts_createds += 1

    def transfer(self, value, favored):
        favored.deposit(value)

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value