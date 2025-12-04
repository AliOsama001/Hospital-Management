from core import Patient
from data import Patient_repo

class Patient_service:
    def login(self, id, password):
        patient = Patient_repo()
        users = patient.loadUsers()
        for i in users["id"]:
            if int(id) == users["id"][i] and password == users["password"][i]:
                self.patient = Patient(i, users)
                return True
        else:
            return False