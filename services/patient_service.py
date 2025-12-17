from core import Patient
from data import Patient_repo
from data import Doctor_repo

class Patient_service:
    def __init__(self, id:int):
        self.patientRepo = Patient_repo()
        self.patient = Patient(self.patientRepo.getPatient(id))

    def bookSchedule(specialization):
        pass