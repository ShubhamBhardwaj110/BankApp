class Bank:

    def __init__(self,bankName):
        self.setBankName(bankName)
        self.accounts = []  

    def getbankName(self):
        return self.bankName
    
    def setBankName(self,bankName):
        if not bankName.strip():
            raise Exception("Name cannot be blank")
        self.bankName = bankName.strip()      
    def openAccount(self):
        pass
    def searchAccount(self):
        pass