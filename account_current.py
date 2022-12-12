class CurrentAccount:
    total_accounts_createds = 0
    tax_operation = None

    def __init__(self, client, agency, number):
        self.__balance = 100
        self.client = client
        self.__agency = agency
        self.__number = number
        CurrentAccount.total_accounts_createds += 1
        CurrentAccount.tax_operation = 30 / CurrentAccount.total_accounts_createds

    @property
    def agency(self):
        return self.__agency

    def __set_agency(self, value):
        if not isinstance(value, int):
            return

        if value <= 0:
            return

        self.__agency = agency

    @property
    def number(self):
        return self.__number

    def __set_number(self, value):
        if not isinstance(value, int):
            return

        if value <= 0:
            return

        self.__number = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, int):
            return

        if value <= 0:
            return

        self.__balance = value

    def transfer(self, value, favored):
        favored.deposit(value)

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value
