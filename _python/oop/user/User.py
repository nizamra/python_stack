class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


lana = User("Lana")
lana.make_deposit(1000)
lana.make_deposit(9720)
lana.make_withdrawal(50)
lana.display_user_balance()

nizam = User("nizam")
nizam.make_deposit(1720)
nizam.make_deposit(2050)
nizam.make_withdrawal(720)
nizam.display_user_balance()



nizam.transfer_money(lana, 1200)
lana.display_user_balance()
nizam.display_user_balance()
