from config import *
import pandas as pd

class Patient_repo:
    def __init__(self):
        self.users = pd.read_csv(PATIENT_CSV)

    def loadUsers(self):
        return self.users.to_dict()
    
    def saveUsers(self, users:dict):
        self.users = pd.DataFrame(users)
        self.users.to_csv(PATIENT_CSV, index=False)