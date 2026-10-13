class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number  # Private attribute for account number
        self.__balance = balance  # Private attribute for balance

    def set_account_number(self, account_number: int):  # Setter method for account number
        if account_number <= 0:
            print("Warning: Account number must be a positive integer.")
            return
        self.__account_number = account_number

    def set_balance(self, balance: float):  # Setter method for balance with validation
        if balance < 0:
            print("Warning: Balance cannot be negative.")
            return
        self.__balance = balance

    @property
    def get_account_number(self):  # Getter method for account number
        return self.__account_number

    def get_balance(self):  # Getter method for balance
        return self.__balance

# OBJECTS

account1 = BankAccount(12112, 9999.99)
account2 = BankAccount(11326, 6767.00)
account3 = BankAccount(13578, 21.00)
account4 = BankAccount(25269, 4358.67)

# OUTPUT

print("OUTPUT 1:")

print()

print("Account 2:")
print(f"Account Number: {account2.get_account_number}")
print(f"Balance: ₱{account2.get_balance():.2f}")

print()

# UPDATE ACCOUNT DETAILS

print(f"Update balance to -1234.56") # Update balance to a negative value
account2.set_balance(-1234.56)

print()

print(f"Account Number: {account2.get_account_number}")
print(f"Balance: ₱{account2.get_balance():.2f}")

print()

print(f"Update balance to ₱1234.56") # Update balance to a positive value   
account2.set_balance(1234.56)

print()
print(f"Account Number: {account2.get_account_number}")
print(f"Balance: ₱{account2.get_balance():.2f}")

print("OUTPUT 2: ")

print()

print("Account 1:")
print(f"Account Number: {account1.get_account_number}")
print(f"Balance: ₱{account1.get_balance():.2f}")

print()

# UPDATE ACCOUNT DETAILS

print(f"Update balance to ₱209.00") # Update balance to a positive value
account1.set_balance(209.00)

print()

print(f"Account Number: {account1.get_account_number}")
print(f"Balance: ₱{account1.get_balance():.2f}")