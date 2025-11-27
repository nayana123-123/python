class BankAccount:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)



account = BankAccount("12345", "Alia", "Savings", 1000)

account.display()
account.deposit(500)
account.withdraw(300)
account.display()
