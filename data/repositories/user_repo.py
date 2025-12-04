import json
from config import *

class User_repo:
    def __init__(self):
        pass

    def loadUsers(self):
        with open(USER_FILE, "r") as f:
            return json.load(f)


    def saveUsers(self, users):
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)