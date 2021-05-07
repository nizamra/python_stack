class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


lana = User("Lana")
lana.make_deposit(1000).make_deposit(9720).make_withdrawal(50).display_user_balance()

nizam = User("nizam")
nizam.make_deposit(1720).make_deposit(2050).make_withdrawal(720).display_user_balance()



nizam.transfer_money(lana, 1200).display_user_balance()
lana.display_user_balance()
