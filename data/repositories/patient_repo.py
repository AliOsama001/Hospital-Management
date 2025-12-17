from config import PATIENT_CSV
import pandas as pd

class Patient_repo:
    def __init__(self):
        self.patients = pd.read_csv(PATIENT_CSV)

    def getPatient(self, id):
        return self.patients[self.patients["id"] == id].to_dict()

    def addPatient(self, id, name, phone, age, specialization, notes, medicine, date, doctor, nextAppointment):
        self.patients.loc[-1] = [id, name, phone, age, specialization, notes, medicine, date, doctor, nextAppointment]

    def saveChanges(self):
        self.patients.to_csv(PATIENT_CSV, index=False)