                                                 #个人答案
"""
class BankAccount:
    def __int__(self, Accountname):
        self.Accountname = accountname
    def Accountnumber(self):
        self.Accountnumber = accountnumber
    def Save(self):
        self.Save = save
    def Take(self):
        self.Take = take
    def Balance(self):
        self.Balance = balance
class InterestAccount(BankAccount):
    
        
save = 10
take = 5
balance = save - take
print "Your balance is: ", balance
print "You have taken money: ", take
print "You have saved money: ", save

"""

                                                    #参考答案
class BankAccount:
    def __int__(self, acct_number, acct_name):
        self.acct_number = acct_number
        self.acct_name = acct_name
        self.balance = 0.0
        
    def displayBalance(self):
        print "The account balance is: ", self.balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print "You deposited ", amount
        print "The new balance is: ", self.balance

    def withdraw(self, amount):
        if self.balance >=amount:
            self.balance = slef.balance - amount
            print "You withdrew ", amount
            print "The new balance is: ", self.blance
        else:
            print "You tried to withdraw ", amount
            print "The account balance is: ", self.balance
            print "Withdrawal denied. Not enough funds."

class InterestAccount(BankAccount):
    def addInterest(self, rate):
        interest = self.balance * rate
        print "Adding interest to the account, ", rate * 100, " percent"
        self.deposit (interest)

#以下为测试代码：

myAccount = InterestAccount(234567, "Carter")
print "Account name: ", myAccount.acct_name
print "Account number: ", myAccount. acct_number
myAccount.displayBalance()
myAccount.deposit(34.52)
myAccount.addinterest(0.11)


