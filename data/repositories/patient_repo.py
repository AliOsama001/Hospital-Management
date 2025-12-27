from config import PATIENT_CSV
import pandas as pd

class Patient_repo:
    def __init__(self):
        self.patients = pd.read_csv(PATIENT_CSV)

    def getPatient(self, id):
        return self.patients[self.patients["id"] == id].to_dict("list")

    def addPatient(self, id, name, phone, age, specialization, notes, medicine, date, doctor, doctorPhone, nextAppointment):
        self.patients.loc[-1] = [id, name, phone, age, specialization, notes, medicine, date, doctor, doctorPhone, nextAppointment]

    def change(self, id, column, value):
        self.patients.loc[self.patients["id"] == id, column] = value

    def updatePatient(self, id, name, phone, age, specialization, notes, medicine, date, doctor, doctorPhone, nextAppointment):
        self.patients.loc[self.patients["id"] == id] = [id, name, phone, age, specialization, notes, medicine, date, doctor, doctorPhone, nextAppointment]

    def saveChanges(self):
        self.patients.to_csv(PATIENT_CSV, index=False)