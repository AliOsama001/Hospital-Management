from core import Doctor, Patient
from data import Doctor_repo, Patient_repo, Schedule_repo
import time

class Doctor_service:
    def __init__(self, id):
        self.patientID = None
        self.doctorRepo = Doctor_repo()
        self.doctor = Doctor(self.doctorRepo.getDoctor(id))
        self.scheduleRepo = Schedule_repo()
        if not self.scheduleRepo.isThereP(self.doctor.getSpecialization()):
            return
        self.patientID, self.scheduleInfo = self.scheduleRepo.nextPatient(self.doctor.getSpecialization())
        self.patientRepo = Patient_repo()
        self.pateint = Patient(self.patientRepo.getPatient(int(self.patientID)))
        self.setPatientInfo()

    def setPatientInfo(self):
        self.pateint.setDoctor(self.doctor.getName())
        self.pateint.setDoctorPhone(self.doctor.getPhone())
        self.pateint.setSpecialization(self.doctor.getSpecialization())
        self.pateint.setDate(time.strftime("%Y-%m-%d"))

    def savePatientInfo(self, notes, medicine, nextAppointment):
        self.patientRepo.updatePatient(
            Patient.getID(self.pateint),
            Patient.getName(self.pateint),
            Patient.getPhone(self.pateint),
            Patient.getAge(self.pateint),
            Patient.getSpecialization(self.pateint),
            notes,
            medicine,
            Patient.getDate(self.pateint),
            Patient.getDoctor(self.pateint),
            Patient.getDoctorPhone(self.pateint),
            nextAppointment
        )
        self.patientRepo.saveChanges()

    def nextPatient(self):
        self.scheduleRepo.deleteBook(self.patientID)
        self.scheduleRepo.saveChanges()
        if not self.scheduleRepo.isThereP(self.doctor.getSpecialization()):
            return None
        self.patientID, self.scheduleInfo = self.scheduleRepo.nextPatient(self.doctor.getSpecialization())
        self.pateint = Patient(self.patientRepo.getPatient(self.patientID))
        self.setPatientInfo()