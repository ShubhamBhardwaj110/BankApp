import bank
class bankApplication:
    def __init__(self):
        self.bank_obj = bank.Bank("KPYL")

    def main(self):
        print("^^^^ WELCOME TO LYPL BANK^^^^\n KINDLY SELECT AN OPTION TO BEGIN\n")
        self.showMainMenu()

    def showMainMenu(self):
        while True:
            print("1. Select Account\n2. Open Account\n3. Exit\n")
            option = int(input("Please enter the option to continue: "))
            if option == 1:
                account_number = int(input("Enter the account number in range (1000,1000000): "))
                account = self.bank_obj.searchAccount(account_number)
                if account is not None:
                    self.showAccountMenu(account)
                else:
                    print("Account not found")


            elif option == 2:
                 self.bank_obj.openAccount()
                        
            else :
                print("exiting")
                break        
        

    def showAccountMenu(self,account):
        while True:
            print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.View Transactions\n5.Exit")
            option = int(input("Please select an option to continue: "))
            if option == 1:
                print(f"Current balance: ${account.getcurrentBalance()}")


            elif option ==2:
                amount = int(input("Please enter the amount to deposit: "))
                account.depositAmount(amount)
                print(f"You have deposited ${amount}")
                print("Remaining Balance: $",account.getcurrentBalance())

            elif option ==3:
                amount = int(input("Please enter the amount to withdraw: "))
                account.withdraw(amount)
                print(f"You have withdrawn ${amount}")
                print("Remaining Balance: $",account.getcurrentBalance())

            elif option ==4:
                pass

            elif option ==5:

                break

appobj = bankApplication()
appobj.main()
