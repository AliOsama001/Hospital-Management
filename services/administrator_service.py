import pandas as pd
from config import PATIENT_CSV, DOCTOR_CSV
from data import User_repo

def read(path_file):
    return pd.read_csv(path_file)

def save_csv(df, path_file):
    df.to_csv(path_file, index=False)

class Administrator_service:
    def __init__(self):
        self.doc = read(DOCTOR_CSV)
        self.pat = read(PATIENT_CSV)
        self.userRepo = User_repo()

    def add_doctor(self, id, name, password, phone, specialization, workHours):
        self.userRepo.addAccount(id, password, "doctor")
        self.userRepo.saveChanges()
        if id in self.doc["id"].values:
            return f"Error: ID {id} already exists"
        new_doctor = pd.DataFrame([{
            "id": id,
            "name": name,
            "phone": phone,
            "specialization": specialization,
            "workHours": workHours
        }])
        self.doc = pd.concat([self.doc, new_doctor], ignore_index=True)
        save_csv(self.doc, DOCTOR_CSV)
        return f"Doctor added successfully with ID: {id}"

    def delete_doctor(self, id):
        self.userRepo.deleteAccount(id)
        self.userRepo.saveChanges()
        if id not in self.doc["id"].values:
            return False
        self.doc = self.doc[self.doc["id"] != id]
        save_csv(self.doc, DOCTOR_CSV)
        return True

    def delete_patient(self, id):
        self.userRepo.deleteAccount(str(id))
        self.userRepo.saveChanges()
        self.doc = read(DOCTOR_CSV)
        if id not in self.pat["id"].values:
            return False
        self.pat = self.pat[self.pat["id"] != id]
        save_csv(self.pat, PATIENT_CSV)
        return True
