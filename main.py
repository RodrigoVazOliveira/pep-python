import sys

from account_current import CurrentAccount
from client import Client

def main():
    accounts = []
    while True:
        try:
            name = input('Digite o nome do cliente: \n')
            agency = input('Digite o número da agência: \n')
            breakpoint()
            number = input('Digite o número da conta: \n')
            client = Client(name, None)
            account_current = CurrentAccount(client=client, agency=agency, number=number)
            accounts.append(account_current)
        except KeyboardInterrupt as e:
            print(f'\n\n{len(accounts)} contas criadas')
            print(e)
            sys.exit()


if __name__ == '__main__':
    main()