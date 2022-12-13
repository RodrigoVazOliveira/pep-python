class CurrentAccount:
    total_accounts_createds = 0
    tax_operation = None

    def __init__(self, client, agency, number):
        self.__balance = 100
        self.client = client
        self.__agency = 0
        self.__number = 0
        CurrentAccount.total_accounts_createds += 1
        CurrentAccount.tax_operation = 30 / CurrentAccount.total_accounts_createds
        self.__set_agency(agency)
        self.__set_number(number)


    @property
    def agency(self):
        return self.__agency

    def __set_agency(self, value):
        if not isinstance(value, int):
            raise AttributeError('O valor não é um número!', value)

        if value <= 0:
            return ValueError('O valor deve ser maior do que zero!')

        self.__agency = value

    @property
    def number(self):
        return self.__number

    def __set_number(self, value):
        if not isinstance(value, int):
            raise AttributeError('O tipo de dado não é um número!', value)

        if value <= 0:
            raise ValueError('O valor deve ser maior o que zero!')

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
