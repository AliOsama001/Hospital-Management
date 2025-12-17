from .person import Person

class Patient(Person):
    def __init__(self, patient:dict):
        super().__init__(patient)
        self.age = patient["age"]
        self.specialization = patient["specialization"]
        self.notes = patient["notes"]
        self.medicine = patient["medicine"]
        self.date = patient["date"]
        self.doctor = patient["doctor"]
        self.nextAppointments = patient["nextAppointment"]

    def getAge(self):
        return self.age

    def getDoctor(self):
        return self.doctor

    def getSpecialization(self):
        return self.specialization

    def getDate(self):
        return self.date
    
    def getMedicine(self):
        return self.medicine

    def getNotes(self):
        return self.notes

    def getAppointments(self):
        return self.next_appointment