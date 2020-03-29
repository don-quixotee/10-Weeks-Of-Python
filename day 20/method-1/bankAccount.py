class Account:
    """ creating a Bank account  with balance"""
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance
        print("Account Created for "+ self.name)
        
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
        self.Show_balance()
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            print("the amount should be more than 500")
        self.Show_balance()
    def Show_balance(self):
        print("balance is {}".format(self.balance))

if __name__ =='__main__':
    Abhishek = Account("Abhishek", 20000)
    # Abhishek.Show_balance()
    Abhishek.deposit(50000)
    # Abhishek.Show_balance()
    Abhishek.withdraw(20000)
    # Abhishek.Show_balance()


    