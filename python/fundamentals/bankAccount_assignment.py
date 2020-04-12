class BankAccount:
    def __init__(self, account_balance, int_rate,):
        self.account_balance = account_balance
        self.int_rate = int_rate
    
    def deposit(self, amount):
        self.account_balance -= amount
        return self

    def withdraw(self, amount):
        self.account_balance += amount
        return self
    
    def display_account_info(self):
        print(self.account_balance)
        print(self.int_rate)
    
    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        # add to account balance the product of account balance and interest rate remember no "*=" because cant have to "=" signs on the same line
        return self

checking = BankAccount(100, .007)
savings = BankAccount(400, .009)

checking.yield_interest().deposit(10).deposit(20).deposit(30).withdraw(5).display_account_info()
savings.deposit(30).deposit(50).withdraw(5).withdraw(10).withdraw(15).withdraw(20).yield_interest().display_account_info()
