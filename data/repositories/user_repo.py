import json
import pandas as pd
from config import *

class User_repo:
    def __init__(self):
        try:
            with open(USER_FILE, "r") as f:
                self.users = json.load(f)
        except:
            self.users = {}

    def loadUsers(self):
        return self.users

    def saveUser(self, id, password, name, age, phone):
        self.users[id] = {"password": password,
                            "role": "patient"
                            }
        self.saveUsers(self.users)
        patients = pd.read_csv(PATIENT_CSV)
        patients.loc[-1] = [id, name, age, phone, "", "", "", "", ""]
        patients.to_csv(PATIENT_CSV)

    def isExist(self, id):
        if id in self.users:
            return True
        else:
            return False

    def saveUsers(self, users):
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)