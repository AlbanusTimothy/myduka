class BankAccount:
    # constructor---initializes objects
    def __init__(self, account_number, balance, owner_name, date_opened):

        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
    # self-references objects
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew {amount}. New balance is {self.balance}"

    def display_info(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Owner: {self.owner_name}\n"
            f"Balance: {self.balance}\n"
            f"Date Opened: {self.date_opened}\n"
        )

    def __str__(self):  
        return f"BankAccount({self.account_number}, Owner={self.owner_name}, Balance={self.balance})"
    


# Create 2 BankAccount objects
acc1 = BankAccount("001234", 5000, "Alba", "2023-05-10")
acc2 = BankAccount("009876", 20000, "Timothy", "2024-01-15")

print(acc1)
print(acc2)

print(acc1.deposit(1500))
print(acc1.withdraw(3000))
print(acc1.display_info())

print(acc2.deposit(5000))
print(acc2.withdraw(10000))
print(acc2.display_info())
