import random
import sys

class ATM():
    def __init__(self, name, account_number, balance = 0):
    #your code here
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.balance = 0
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")

        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        #your code here
    def deposit(self, amount):
        #your code here with suitable messages to the user
        self.balance += amount
        print(f"Deposited Nu.{amount}. New balance is Nu.{self.balance}")

    def withdraw(self, amount):
        #your code here. Negative balance allowed but should be a message saying     you have become overdrawn
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of Nu.{amount} successful. New balance is Nu.{self.balance}")
        else:
            print("Error: Insufficient funds!")

    def check_balance(self):
    #your code here
        print(f"Current Balance: Nu.{self.balance}")

    def transaction(self):
        print("""
        TRANSACTION
        *********************
        Menu:
        1. Account Detail
        2. Check Balance
        3. Deposit
        4. Withdraw
        5. Exit
        *********************
        """)
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                    printing receipt..............
                    ******************************************
                    Transaction is now complete.
                    Transaction number: {random.randint(10000, 1000000)}
                    Account holder: {self.name.upper()}
                    Account number: {self.account_number}
                    Available balance: Nu.{self.balance}
                    Thanks for choosing us as your bank
                    ******************************************
                    """)
                    sys.exit()
print("*******WELCOME TO BANK OF CSIT UCC*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")

atm = ATM(name, account_number)

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
    | Thanks for choosing us as your bank |
    | Visit us again! |
    -------------------------------------
    """)
        break
    else:
        print("Wrong command! Enter 'y' for yes and 'n' for NO.\n")