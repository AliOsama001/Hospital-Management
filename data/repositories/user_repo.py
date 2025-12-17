from config import USER_JSON
import json

class User_repo:
    def __init__(self):
        try:
            with open(USER_JSON, "r") as f:
                self.users = json.load(f)
        except:
            self.users = {}

    def isExist(self, id):
        return id in self.users

    def getPassword(self, id):
        return self.users[id]["password"]
    
    def getRole(self, id):
        return self.users[id]["role"]
    
    def addAccount(self, id, password, role):
        self.users[id] = {
            "password": password,
            "role": role
        }

    def saveChanges(self):
        with open(USER_JSON, "w") as f:
            json.dump(self.users,f)