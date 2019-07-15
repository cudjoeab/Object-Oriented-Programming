class BankAccount: 

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def __str__(self):
        return(f"Your balance is {self.balance} at an interest rate of {self.interest_rate}.")

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount): 
        self.balance -= amount

    def gain_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return(f"Your total balance is {self.balance}.")

account1 = BankAccount(1000, 0.16)
print(account1)

account1.deposit(50)
print(account1)

account1.withdraw(50)
print(account1)

account1.gain_interest()
print(account1)






