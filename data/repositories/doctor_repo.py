from config import DOCTOR_CSV
import pandas as pd

class Doctor_repo:
    def __init__(self):
        self.doctors = pd.read_csv(DOCTOR_CSV)

    def getDoctor(self, id):
        return self.doctors[self.doctors["id"] == id].to_dict("list")

    def saveChanges(self):
        self.doctors.to_csv(DOCTOR_CSV, index=False)

    def loadDoctors(self):
        return self.doctors[["name", "phone", "specialization", "workHours"]].to_dict()

    def getSpecializations(self):
        return self.doctors["specialization"].values

    def getDoctorsName(self, specialization):
        return self.doctors["name"][self.doctors["specialization"] == specialization].values