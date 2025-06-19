import csv
import constants as CONST 

class User:
    @staticmethod
    def writeUser(userName, userID, newPassword):
        with open(CONST.userInfoFile, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([userName, userID, newPassword, 0])
    @staticmethod
    def getLatestID(latestIDFile):
        with open(latestIDFile, 'r') as file:
            latestID = file.read().strip()
        return int(latestID)
    @staticmethod
    def checkPassword(username, password):
        with open(CONST.userInfoFile, 'r') as file: 
            for line in file:
                user = line.strip().split(',')[0]
                if user == username:
                    userPassword = line.strip().split(',')[2]
                    if userPassword == password:
                        return True
                    else: 
                        return False
        