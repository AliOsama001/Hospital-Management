from data import User_repo
from data import Patient_repo

class User_service:
    def __init__(self):
        self.userRepo = User_repo()
        self.patientRepo = Patient_repo()

    def login(self, id, password):
        if self.userRepo.isExist(id) and password == self.userRepo.getPassword(id):
            return self.userRepo.getRole(id)
        return ""

    def regiter(self, id, password, name , age , phone):
        if self.userRepo.isExist(id):
            return False
        self.userRepo.addAccount(id, password, "patient")
        self.userRepo.saveChanges()
        self.patientRepo.addPatient(id, name, age, phone, "", "", "", "", "", "")
        self.patientRepo.saveChanges()
        return True