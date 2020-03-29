import datetime
import pytz

class Account:


    """ creating a Bank account  with balance"""
    @staticmethod
    def _current_time():
        """ """
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__ (self, name, balance):

        self.name = name
        self.balance = balance
        self.transaction_List = []
        print("Account Created for "+ self.name)
        
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
        self.Show_balance()
        self.transaction_List.append((Account._current_time(), amount))


    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self.transaction_List.append((Account._current_time(),amount))
        else:
            print("the amount should be more than 500")
        self.Show_balance()

    def Show_balance(self):
        print("balance is {}".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_List:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "{withdrawn"
            print("{:6} {} on {} \n (local time was:-  {})".format(amount, tran_type, date, date.astimezone() ))

if __name__ =='__main__':
    print()
    Abhishek = Account("Abhishek", 20000)
    # Abhishek.Show_balance()
    Abhishek.deposit(50000)
    # Abhishek.Show_balance()
    Abhishek.withdraw(20000)
    # Abhishek.Show_balance()
    print()
    Abhishek.show_transaction()
    


    