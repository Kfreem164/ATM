class Account:
    def __init__(self, ID=0, account=100, annualInterestRate=0):
        self.ID = ID
        self.account = account
        self.annualInterestRate = annualInterestRate

    def setID(self, ID):
        self.ID = ID

    def setAccount(self, account):
        self.account = account

    def setAnnualInterestRate(self, annualInterestRate):
        self.annualInterestRate = annualInterestRate

    def getID(self):
        return self.ID

    def getAccount(self):
        return self.account

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def getMonthlyInterestRate(self):
        rate = self.annualInterestRate/12
        return rate
        
    def getMonthlyInterest(self):
        monthlyInt = self.annualInterestRate/12
        interest = monthlyInt * self.account
        return interest

    def withdraw(self, amount):
        if amount <= self.account:
            self.account -= amount
        else:
            return print("Unsucccesful withdrawl")

    def deposit(self, amount):
        self.account += amount
        
def main():
    accounts = [Account(ID=i, account = 100) for i in range(10)]

    while True:
        userId = int(input("\nEnter ID number: "))
        if userId >= 0 and userId <10:
            account = accounts[userId]

            while True:
                print("\nMain Menu")
                print("1: Check balance")
                print("2: withdraw")
                print("3: deposit")
                print("4: exit")

                choice = input("Enter a choice: ")

                if choice == "1":
                    print (f"The balance is ${account.getAccount()}")

                elif choice == "2":
                    amount = int(input("How much would you like to withdraw?: "))
                    account.withdraw(amount)
                        
                elif choice == "3":
                    amount = int(input("How much would you like to deposit?: "))
                    account.deposit(amount)

                elif choice == "4":
                    break

                else:
                    print("Invalid choice")
        else:
            print("ID entered incorrectly, please try again")


main()
    
