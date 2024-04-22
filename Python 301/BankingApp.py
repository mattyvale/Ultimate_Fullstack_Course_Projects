from decimal import *
from insert import new_customer
from update import update_balance
from usercheck import check_user, new_user_check

class User():
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def show_user(self):
        print("Current User:")
        print("") 
        print(self.name)

class Bank(User):
        def __init__(self, id, name, balance):
            super().__init__(id, name, balance)

        def deposit(self, amount):
            self.amount = amount
            self.balance = self.balance + self.amount
            update_balance(self.id, self.balance)
            print("You have successfully deposited $" + str(self.amount) + ".\nYour new balance is $" + str(self.balance)) 

        def withdraw(self, amount):
            self.amount = amount
            if self.amount > self.balance:
                print("Insufficient funds to complete your transaction. Current balance available is $" + str(self.balance))
            else:
                self.balance = self.balance - self.amount
                update_balance(self.id, self.balance)
                print("You have successfully withdrawn $" + str(self.amount) + ".\nYour current balance remaining is $" + str(self.balance))

        def viewBalance(self):
            print("Your current balance is $" + str(self.balance))

def login():
    main = True
    while main == True:
        loginID = int(input("Enter your user ID:"))
        loginPin = int(input("Enter your pin:"))
        isUserValid = check_user(loginID, loginPin)
        if isUserValid is None:
            while True:
                loginRetry = input("User ID or Pin is invalid! Would you like to continue (Y/N)")
                if loginRetry == 'Y':
                    break
                elif loginRetry == 'N':
                    main = False
                    break
                else:
                    print("Please Press Y or N")
        else:
            while True:
                user = Bank(int(isUserValid[0]), isUserValid[1], Decimal(isUserValid[2].strip('$')))
                userOptions = input("Please select from the following options:\n1. Deposit\n2. Withdraw\n3. View Balance\nPress E to exit to main menu.\n")
                if userOptions == '1':
                    newDeposit = Decimal(input("How much would you like to deposit?\n"))
                    user.deposit(newDeposit)
                elif userOptions == '2':
                    newWithdrawal = Decimal(input("How much would you like to withdraw?\n"))
                    user.withdraw(newWithdrawal)
                elif userOptions == '3':
                    user.viewBalance()
                elif userOptions == 'E':
                    main = False
                    break
                else:
                    print("Invalid selection!")

def newUser():
    while True:
        userID = int(input("Please enter a unique ID:\n"))
        newUserCheck = new_user_check(userID)
        print(newUserCheck)
        if newUserCheck is not None:
            option = input("Sorry user ID is already in use! Press E if you would like to exit or any other key to try again.\n")
            if option == 'E':
                break
            else:
                continue
        else:
            userName = input("Please enter a username:\n")
            userPin = int(input("Please enter a pin:\n"))
            balance = 0
            new_customer(userID, userName, userPin, balance)
            login()
            break

while True:
    welcomeScreen=input("Welcome to OneBank! Please choose from the following options:\n1. Login (Existing Customers)\n2. Sign up(New Customers)\nPress E to exit the app.\n")
    if(welcomeScreen == '1'):        
        login()
    elif(welcomeScreen == '2'):
        newUser()
    elif(welcomeScreen == 'E'):
        break
    else:
        print("Invalid selection!")