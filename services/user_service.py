from data import User_repo
from data import Patient_repo

class User_service:
    def __init__(self):
        self.userRepo = User_repo()
        self.patientRepo = Patient_repo()

    def login(self, id, password):
        if self.userRepo.isExist(id) and password == self.userRepo.getPassword(id):
            return self.userRepo.getRole(id)
        return None

    def regiter(self, id, password, name , phone , age):
        if self.userRepo.isExist(id):
            return False
        self.userRepo.addAccount(id, password, "patient")
        self.userRepo.saveChanges()
        self.patientRepo.addPatient(id, name, phone, age, "", "", "", "", "", "", "")
        self.patientRepo.saveChanges()
        return True

    def verifyPassword(self, id, old_password):
        return self.userRepo.isExist(id) and old_password == self.userRepo.getPassword(id)

    def changePassword(self, id, new_password):
        if self.userRepo.isExist(id):
            self.userRepo.updatePassword(id, new_password)
            self.userRepo.saveChanges()
            return True
        return False

    def addDoc(self, id, password):
        self.userRepo.addAccount(id, password, "doctor")