from core import Doctor, Patient
from data import Doctor_repo, Patient_repo, Schedule_repo
import time

class Doctor_service:
    def __init__(self, id):
        self.doctorRepo = Doctor_repo()
        self.doctor = Doctor(self.doctorRepo.getDoctor(id))
        self.scheduleRepo = Schedule_repo()
        try:
            self.patentID, self.scheduleInfo = self.scheduleRepo.nextPatient(self.doctor.getSpecialization())
        except:
            self.patentID = None
        self.patientRepo = Patient_repo()
        self.pateint = Patient(self.patientRepo.getPatient(int(self.patentID)))
        self.setPatientInfo()

    def setPatientInfo(self):
        self.pateint.setDoctor(self.doctor.getName())
        self.pateint.setDoctorPhone(self.doctor.getPhone())
        self.pateint.setSpecialization(self.doctor.getSpecialization())
        self.pateint.setDate(time.strftime("%Y-%m-%d"))
        self.pateint.setDoctorPhone(self.doctor.getPhone())

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
        self.patentID, self.scheduleInfo = self.scheduleRepo.nextPatient(self.doctor.getSpecialization())
        if self.patentID is None:
            return None
        self.scheduleRepo.deleteBook(self.patentID)
        self.scheduleRepo.saveChanges()
        self.pateint = Patient(self.patientRepo.getPatient(self.patentID))
        self.setPatientInfo()