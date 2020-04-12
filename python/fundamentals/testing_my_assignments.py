class User:
    def __init__(self, first_name, last_name, account):
        self.first_name = first_name
        self.last_name = last_name
        self.account = account
    
    def make_deposit(self, amount):
        self.account += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account -= amount
        return self
    
    def display_user_balance(self):
        print(self.first_name)
        print(self.last_name)
        print(self.account)
        return self
    
    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        return self



user1= User("Ray", "Robinson", 60)
user2= User("Ezra", "Song", 150)
user3= User("Alijah", "Smith", 100)

user1.make_withdrawal(50).display_user_balance()
user1.make_deposit(20).display_user_balance()


user1.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(20).display_user_balance()

user2.make_deposit(1000).make_deposit(600).make_withdrawal(30).make_withdrawal(40).display_user_balance()

user3.make_deposit(7000).make_withdrawal(1000).make_withdrawal(200).make_withdrawal(300).display_user_balance()
user1.transfer_money(user3, 50).display_user_balance()
print(user3.first_name)
print(user3.account)