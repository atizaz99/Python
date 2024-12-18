class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f'Deposited: {amount}. New Balance: {self.balance}')
        else:
            print('Invalid deposit amount')
        
        def withdraw(self, amount):
            if 0<amount <=self.balance:
                self.balance -= amount
                print(f'Withdrawn: {amount}. New Balance: {self.balance}')
            else:
                print('Invalid withdrawal amount.')

        def display_details(self):
            print(f'Account Number: {self.account_number}, Account Name: {self.account_name}')
            print(f'Balance: {self.balance}')
        

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name):
        if account_number in self.accounts:
            print('Account already exists')
        else:
            self.accounts[account_number] = BankAccount(account_number, account_name)
            print(f'Account created for {account_name}')

    
    def transfer_funds(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >=amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                print('Transfer completd successfully.')

            else:
                print('Insufficient funds')
        else:
            print('Invalid account number')
        
    def list_accounts(self):
        for account in self.accounts.values():
            account.display_details()
        
def main():
    bank_system = BankSystem()
    while True:
        print('''
        Banking System Menu
        1. Create New Account
        2. Deposit Funds
        3. Withdraw Funds
        4. Transfer Funds
        5. Display Account Details
        6. Exit
    
        ''')
        choice = input('Enter your choice:')
        if choice == '1':
            account_number = input('Enter account number: ')
            account_name = input('Enter account name: ')
            bank_system.create_account(account_number, account_name)
        elif choice == '2':
            account_number = input('Enter account number: ')
            amount = float(input('Enter amount to deposit'))
            if account_number in bank_system.accounts:
                bank_system.accounts[account_number].deposit(amount)
            else:
                print('Account not found')
        
        elif choice == '3':
            account_number = input('Enter account number: ')
            amount = float(input('Enter amount to withdraw'))
            if account_number in bank_system.accounts:
                bank_system.accounts[account_number].withdraw(amount)
            else:
                print('Account not found')
        elif choice == '4':
            from_acc = input('Enter account number to transfer from: ')
            to_acc = input('Enter account number to transfer to: ')
            amount = float(input('Enter amount to transfer'))
            bank_system.transfer_funds(from_acc, to_acc, amount)
        elif choice == '5':
            bank_system.list_accounts()
        elif choice == '6':
            break
        else:
            print('Invalid choice, please try again')
        
if __name__ == '__main__':
    main()

