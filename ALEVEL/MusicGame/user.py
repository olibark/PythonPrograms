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