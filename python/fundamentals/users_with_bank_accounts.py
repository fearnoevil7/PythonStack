class BankAccount:
    def __init__(self, account_balance, int_rate,):
        self.account_balance = account_balance
        self.int_rate = int_rate
    
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    
    def display_account_info(self):
        print(self.account_balance)
        return self
        #print(self.int_rate)
    
    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        # add to account balance the product of account balance and interest rate remember no "*=" because cant have to "=" signs on the same line
        return self

class User:
    def __init__(self, first_name, last_name, balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.account = BankAccount(int_rate = 0.05, account_balance = balance)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.first_name)
        print(self.last_name)
        self.account.display_account_info()
        return self

    # def display_account_info(self):
    #     self.account.display_account_info()
        # print(self.account.account_balance)
    
    # def transfer_money(self, other_user, amount):
    #     self.account -= amount
    #     other_user.account += amount
    #     return self

user1= User("Ray", "Robinson")
# user1.display_account_info()
# user2= User("Ezra", "Song", 150)
# user3= User("Alijah", "Smith", 100)


# checking = BankAccount(100, .007)
# savings = BankAccount(400, .009)

# user1.display_user_balance()

# user1.make_deposit(20)
user2 = User("Jon", "Song", 500)
user1.make_deposit(20).make_withdrawal(5).display_user_balance()
user2.make_deposit(30).make_withdrawal(7).display_user_balance()
