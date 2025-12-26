from core import Patient, Schedule
from data import Patient_repo, Doctor_repo, Schedule_repo

class Patient_service:
    def __init__(self, id:int):
        self.patientRepo = Patient_repo()
        self.patient = Patient(self.patientRepo.getPatient(id))
        self.doctorRepo = Doctor_repo()
        self.scheduleRepo = Schedule_repo()
        schedule = self.scheduleRepo.getSchedule(self.patient.getID())
        if schedule is None:
            self.schedule = Schedule(self.patient.getID(), {"specialization": "", "doctorName": "", "date": ""})
        else:
            self.schedule = Schedule(self.patient.getID(), schedule)

    def bookSchedule(self, specialization, doctor, date):
        if self.scheduleRepo.isBooked(str(self.patient.getID())):
            return False
        self.schedule.setSpecialization(specialization)
        self.schedule.setDoctor(doctor)
        self.schedule.setDate(date)
        self.scheduleRepo.addBook(self.patient.getID(), specialization, doctor, date)
        self.scheduleRepo.saveChanges()
        self.patient.setAppointment(date)
        self.patientRepo.change(self.patient.getID(), "nextAppointment", date)
        self.patientRepo.saveChanges()
        return True
    
    def deleteSchedule(self):
        self.schedule.setSpecialization("")
        self.schedule.setDoctor("")
        self.schedule.setDate("")
        self.scheduleRepo.deleteBook(str(self.patient.getID()))
        self.scheduleRepo.saveChanges()
        self.patient.setAppointment("")
        self.patientRepo.change(self.patient.getID(), "nextAppointment", "")
        self.patientRepo.saveChanges()

    def getSpecializations(self):
        return list(set(self.doctorRepo.getSpecializations()))

    def getDoctors(self, specialization):
        return self.doctorRepo.getDoctorsName(specialization)