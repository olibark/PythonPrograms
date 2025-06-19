import os
import constants as CONST
from user import User

class Menu():
    @staticmethod
    def clear():
        os.system('clear')
    @staticmethod
    def printMenu(signedInAs):
        try: 
            if signedInAs is not None: 
                print(signedInAs)
        except:
            signedInAs = None
            print("Not signed in")
        Menu.clear()
        print("1: Register")
        print("2: Sign In")
        print("3: Display User Names")
        print("4: Display High Scores")
        choice = int(input(""))
        if choice == 1:
            Menu.addUser()
        elif choice == 2:
            signedInAs = Menu.signIn()
        elif choice == 3:
            Menu.displayUsers()
        elif choice == 4:
            Menu.displayHighScores()
        else:
            print("Invalid option. Please try again.")
    @staticmethod
    def addUser():
        userName = input("Enter your name: ")
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
                signedInAs = username
                searching = False
                print("You are now signed in.")
                input()
                return signedInAs
            else: 
                print("Invalid")
                return
