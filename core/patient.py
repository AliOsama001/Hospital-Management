from .person import Person

class Patient(Person):
    def __init__(self, patient:dict):
        super().__init__(patient)
        self.age = patient["age"][0]
        self.specialization = patient["specialization"][0]
        self.notes = patient["notes"][0]
        self.medicine = patient["medicine"][0]
        self.date = patient["date"][0]
        self.doctor = patient["doctor"][0]
        self.doctorPhone = patient["doctorPhone"][0]
        self.nextAppointment = patient["nextAppointment"][0]

    def getAge(self):
        return self.age

    def getSpecialization(self):
        return self.specialization

    def getNotes(self):
        return self.notes

    def getMedicine(self):
        return self.medicine

    def getDate(self):
        return self.date

    def getDoctor(self):
        return self.doctor

    def getDoctorPhone(self):
        return self.doctorPhone

    def getAppointment(self):
        return self.nextAppointment

    def setAppointment(self, date):
        self.nextAppointment = date

    def setSpecialization(self, specialization):
        self.specialization = specialization

    def setDoctor(self, doctor):
        self.doctor = doctor

    def setDoctorPhone(self, phone):
        self.doctorPhone = phone

    def setNotes(self, notes):
        self.notes = notes

    def setMedicine(self, medicine):
        self.medicine = medicine

    def setDate(self, date):
        self.date = date