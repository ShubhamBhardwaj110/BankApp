class Account:
    def __init__(self,accountNumber, accountHolderName, currentBalance):
        self.currentBalance = currentBalance
        self.rateOfInterest = float(2.5)
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName



    def getAccountNumber(self):
        return self.accountNumber
    
    def getAccountHolderName(self):
        return self.accountHolderName
    
    def setAccountNumber(self,accountNumber:int):
        if     1000<= self.accountNumber <= 10000:
            raise Exception("Account number should be in the range (1000,10000)")
        self.accountNumber = accountNumber

    def setAccountHolderName(self,accountHolderName):
        if not accountHolderName.strip():
            raise Exception("Name should not be blank")
        self.accountHolderName = accountHolderName.title()

    def getcurrentBalance(self):
        return self.currentBalance
    

