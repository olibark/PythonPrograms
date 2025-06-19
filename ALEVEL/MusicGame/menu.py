import os
import constants as CONST
from user import User

class Menu():
    @staticmethod
    def printMenu(latestIDFile):
        os.system('clear')
        print("1: Register")
        print("2: Display User Info")
        print("3: Display User Names")
        print("4: Display High Scores")
        choice = int(input(""))
        if choice == 1:
            Menu.addUser()
        elif choice == 2:
            Menu.displayUserInfo()
        elif choice == 3:
            Menu.displayUserNames()
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