# Create a BankAccount class with the attributes interest rate and balance 
class BankAccount:
    def __init__(self, intRate, balance=0):
        self.balance = balance
        self.intRate = intRate

# Add a deposit method to the BankAccount class
    def deposit(self, amount):
        self.balance += amount
        return self

# Add a withdraw method to the BankAccount class
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

# Add a display_account_info method to the BankAccount class
    def displayAccountInfo(self):
        print(f'Balance: ${self.balance}')
        return self

# Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        if(self.balance >= 0):
            self.balance += self.balance*self.intRate
        return self

# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
checking = BankAccount(0.01).deposit(545).deposit(202).deposit(2001).withdraw(1200).yield_interest().displayAccountInfo()

# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
savings = BankAccount(0.02, 500).deposit(1000).deposit(2430).withdraw(27).withdraw(80).withdraw(400).withdraw(35).yield_interest().displayAccountInfo()