class BankAccount:
    bankid=100
    def __init__(self,name, int_rate=0.01, balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        self.accid=BankAccount.bankid
        print(f"Dear {self.name} your new account number is: {BankAccount.bankid}, balance:{self.balance}$")
        BankAccount.bankid+=1
    def deposit(self, amount, id):
        self.balance += amount
        return self
    def withdraw(self, amount, id):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}$, Account Number: {self.accid}")
        return self
    def interest(self):
        self.balance *= self.int_rate
        return self
    def transfer_money(self, amount, id, other_user):
        self.balance -= amount
        other_user.balance += amount
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name,int_rate=0.02, balance=0)

    

lana = User("Lana Yaghi","yaghi.l@gmail.com")
nizam = User("Nizam","nizamra")
rachel = User("Rachel","rachelp5446@gmail.com")
kilo = User("Kilo","kilo@dogmail.com")
nizam = User("Nizam","nizamra")
print()
print(locals())
# lana.deposit(1340).withdraw(500).display_user_balance()
# nizam.deposit(5300,101).withdraw(650,101).display_user_balance()
# lana.deposit(1340).withdraw(500).display_user_balance()
# rachel.display_user_balance()