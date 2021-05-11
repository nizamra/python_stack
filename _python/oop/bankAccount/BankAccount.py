class BankAccount:
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        if amount<self.balance:
            self.balance -= amount
        else:
            self.balance -= 5
            print ("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self


lana = BankAccount(2350)
lana.make_deposit(1340).make_deposit(9720).make_deposit(850).make_withdrawal(500).display_account_info()

nizam = BankAccount(1680)
nizam.make_deposit(4720).make_deposit(2050).make_withdrawal(720).make_withdrawal(720).make_withdrawal(720).make_withdrawal(720).yield_interest().display_account_info()