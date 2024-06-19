from bank import Bank

# Example usage
if __name__ == "__main__":
    bank = Bank()
    bank.create_account("123", "Alice", 100.0)
    bank.create_account("456", "Bob", 50.0)

    bank.deposit_to_account("123", 50.0)
    bank.withdraw_from_account("456", 20.0)

    print(bank.get_account_balance("123"))
    print(bank.get_account_balance("456"))

    print(bank)
