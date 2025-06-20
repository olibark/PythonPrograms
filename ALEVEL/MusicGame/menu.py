import os
import constants as CONST
from user import User

class Menu():
    signedIn = False
    signedInAs = None
    @staticmethod
    def clear():
        os.system('clear')
    @staticmethod
    def printMenu():
        Menu.clear()
        if Menu.signedIn: 
            print(Menu.signedInAs)
        else: 
            print("Guest")
        print("1: Register")
        print("2: Sign In")
        print("3: Display User Names")
        print("4: Display High Scores")
        choice = int(input(""))
        if choice == 1:
            Menu.addUser()
        elif choice == 2:
            user = Menu.signIn()
            if user:
                Menu.signedIn = True
                Menu.signedInAs = user
            else:
                print("Sign in failed.")
                input()
        elif choice == 3:
            Menu.displayUsers()
        elif choice == 4:
            Menu.displayHigh()
        else:
            print("Invalid option. Please try again.")
    @staticmethod
    def displayHigh():
        Menu.clear()
        with open(CONST.userInfoFile, 'r') as file:
            for line in file: 
                if line.startswith("userName"):
                    continue
                else: 
                    data = line.strip().split(',')
                    userName = data[0]
                    highScore = data[3]
                    print(f"{userName}: {highScore}")
            input()
    @staticmethod
    def addUser():
        userName = input("Enter your user: ")
        userID = User.getLatestID(CONST.latestIDFile) + 1
        with open(CONST.latestIDFile, 'w') as file:
            file.write(str(userID))
        newPassword = input("Enter your password: ")
        User.writeUser(userName, userID, newPassword)
        print(f"User {userName} registered with ID {userID}.")
        input()
    @staticmethod
    def displayUsers():
        Menu.clear()
        with open(CONST.userInfoFile, 'r') as file:
            users = file.readlines()
        for user in users:
            line = user.strip().split(',')[0]
            if line.startswith("userName"):
                pass
            else:
                print(line)
        input("Press Enter to continue...")
    @staticmethod
    def signIn():
        Menu.clear()
        searching = True
        while searching: 
            username = input("Username: ")
            password = input("Password: ")
            if User.checkPassword(username, password):
                print(f"Welcome {username}")
                signedIn = True
                signedInAs = username
                searching = False
                print("You are now signed in.")
                input()
                return signedInAs
            else: 
                print("Invalid")
                return
