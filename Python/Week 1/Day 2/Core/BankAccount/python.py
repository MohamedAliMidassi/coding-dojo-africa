class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        amount+=5
        print("succssesful deposit")
    def withdraw(self, amount):
        # your code here
        print("Insuffcient funds: Charging a $5 fee")
        amount-=5
    def display_account_info(self):
        # your code here
        print("Balance : $100")
    def yield_interest(self):
        # your code here
        if(self.balance>0):
            self.balance+=0.01
            print("the intrest rate increased")
account1=BankAccount(0.1,1)
account1.deposit(5)
account1.withdraw(5)
account1.display_account_info()
account1.yield_interest()