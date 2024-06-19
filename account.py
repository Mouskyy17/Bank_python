
# For handling transaction errors
class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

class Account:
   
    # Initializes an account with an account number, owner, and initial balance.
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # Adds an amount to the account balance
    def deposit(self, amount):
        if amount <= 0:
            raise TransactionError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    # Withdraw an amount from the account balance
    def withdraw(self, amount):
        if amount <= 0:
            raise TransactionError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise TransactionError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")

    # Returns the current account balance
    def get_balance(self):
        return self.balance

    # Returns a string representation of the account
    def __str__(self):
        return f"Account {self.account_number} owned by {self.owner} has balance: {self.balance:.2f}"