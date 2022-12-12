from account_current import CurrentAccount
from client import Client

client = Client('Rodrigo', '243242323')
current_account = CurrentAccount(client, 100, 1001)
print(f'Agência: {current_account.agency} e o número da conta: {current_account.number}')
