import savingsAccount
import chequingAccount
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
        while True:
            print("Welcome! In order to create an account, please select an option to continue")
            print("1. Open Savings Account")
            print("2. Open Chequing Account")
            print("3. Exit\n")
            choice = int(input("Enter the choice: "))
            if choice ==1:
                print("************WELCOME TO YOUR SAVINGS ACCOUNT************")
                accountNumber = int(input("Please enter your Account Number: "))
                accountHolderName = input("Please enter your name: ")
                amount = int(input("Pleae enter the amuount: $"))
                savingsAccountObj1= savingsAccount.SavingsAccount(accountNumber,accountHolderName,amount)
                self.accounts.append(savingsAccountObj1)
                print(savingsAccountObj1)
                print(self.accounts)
                break

            elif choice ==2:
                print("************WELCOME TO YOUR CHEQUING ACCOUNT************")
                accountHolderName = input("Please enter your name: ")
                accountNumber = int(input("Please enter your Account Number: "))
                amount = int(input("Please enter the amount: $"))
                chequingAccountObj1= chequingAccount.ChequingAccount(accountNumber,accountHolderName,amount)
                self.accounts.append(chequingAccountObj1)
                print(chequingAccountObj1)  
                print(self.accounts)
                return self.accounts

            elif choice ==3:
                print("exit")
                return self.accounts




    def searchAccount(self,accountNumber):
        for accountNumberobj in self.accounts:
            if accountNumberobj.getAccountNumber() == accountNumber:  
                print(f"AccountNumber: {accountNumber}")
                return accountNumberobj
        print("Account does not exist")
        return None