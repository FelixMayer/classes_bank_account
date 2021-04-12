# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

#     - increases the account balance by the given amount
#     - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
#     - print to the console
#     - increases the account balance by the current balance * the interest rate (as long as the balance is positive)


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

account1 = BankAccount(0.02, 200)
account2 = BankAccount(0.01, 50)
account3 = BankAccount(0.03, 20)

account1.deposit(100).deposit(50).deposit(75).withdraw(25).yield_interest().display_account_info()
account2.deposit(25).deposit(300).withdraw(25).withdraw(15).withdraw(20).withdraw(15).yield_interest().display_account_info()
account3.withdraw(30)
account3.display_account_info()