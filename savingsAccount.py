import account

class SavingsAccount(account.Account):
    def __init__(self, accountNumber, accountHolderName, currentBalance):
        super().__init__(accountNumber, accountHolderName, currentBalance)
        self.minimumBalance = -1000


    def getMinimumBalance(self):
         return self.minimumBalance
    
    def withdraw(self,withdrawAmount):
        if withdrawAmount >= self.currentBalance or withdrawAmount> self.minimumBalance:
            raise Exception("Please enter the valid amount")
        self.currentBalance = self.currentBalance - withdrawAmount
        return  self.currentBalance 