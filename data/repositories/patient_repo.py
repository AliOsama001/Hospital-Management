from config import *
import pandas as pd
import json

class Patient_repo:
    def __init__(self):
        self.data = pd.read_csv(PATIENT_CSV)
        try:
            with open(SCHEDULE_FILE, "r") as f:
                self.schedule = json.load(f)
        except:
            self.schedule = {}

    def loadUsers(self):
        return self.data.to_dict()

    def saveUsers(self, users):
        self.data = pd.DataFrame(users)
        self.data.to_csv(PATIENT_CSV, index=False)

    def addAppointment(self, id, specialization):
        for i in self.schedule:
            if id == int(i):
                return False
        self.schedule[id] = {"specialization": specialization}
        with open(SCHEDULE_FILE, "w") as f:
            json.dump(self.schedule, f, indent=4)
        return True