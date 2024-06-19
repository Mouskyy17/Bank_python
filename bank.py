from account import Account, TransactionError

class Bank:
    # Initializes a bank with an account dictionary.
    def __init__(self):
        self.accounts = {}

    # Creates a new account with an account number, owner and initial balance.
    def create_account(self, account_number, owner, initial_balance=0.0):
        if account_number in self.accounts:
            raise TransactionError("Account number already exists.")
        self.accounts[account_number] = Account(account_number, owner, initial_balance)
        print(f"Created account {account_number} for {owner} with initial balance {initial_balance:.2f}")

    # Returns the account associated with an account number
    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise TransactionError("Account not found.")
        return self.accounts[account_number]

    # Makes a deposit into a specific account.
    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)

    # Make a withdrawal to a specific account
    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        account.withdraw(amount)

    # Returns the balance of a specific account
    def get_account_balance(self, account_number):
        account = self.get_account(account_number)
        return account.get_balance()

    # Returns a string representation of all accounts in the bank
    def __str__(self):
        return "\n".join(str(account) for account in self.accounts.values())