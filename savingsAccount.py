import account

class ChequingAccount(account.Account):
    def __init__(self, accountNumber, accountHolderName, currentBalance):
        super().__init__(accountNumber, accountHolderName, currentBalance)
        self.overdraftlimit = -5000


    def getoverdraftLimit(self):
         return self.overdraftlimit
    
    def withdraw(self,amount):
        if self.currentBalance - amount >= self.overdraftlimit:
            self.currentBalance -= amount
        else:
            raise Exception("Please enter the valid amount")
        return  self.currentBalance 