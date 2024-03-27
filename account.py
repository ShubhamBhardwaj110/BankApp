class Account:
    def __init__(self,accountNumber, accountHolderName, currentBalance):
        self.currentBalance = currentBalance
        self.rateOfInterest = float(2.5)
        self.setAccountNumber(accountNumber)
        self.setAccountHolderName(accountHolderName)



    def getAccountNumber(self):
        return self.accountNumber
    
    def getAccountHolderName(self):
        return self.accountHolderName
    
    def setAccountNumber(self,accountNumber:int):
        if     1000<= accountNumber <= 10000:
            raise Exception("Account number should be in the range (1000,10000)")
        self.accountNumber = accountNumber

    def setAccountHolderName(self,accountHolderName):
        if not accountHolderName.strip():
            raise Exception("Name should not be blank")
        self.accountHolderName = accountHolderName.title()

    def getcurrentBalance(self):
        return self.currentBalance
    
    def depositAmount(self,amount):
        if amount > 0:
            self.currentBalance+=amount
        else:
            return "Please enter the valid amount"
        
    def __str__(self):
        return f"\n****Account Updated**** \n Name: {self.getAccountHolderName()}\n|\n Account Number: {self.getAccountNumber()}\n|\n Balance: ${self.currentBalance}\n"
        
    
    def withdraw(self):
        raise NotImplementedError("Defined in saving and chequing class")
    

