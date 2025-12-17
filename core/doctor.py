from .person import Person

class Doctor(Person):
    def __init__(self, doctor:dict):
        super().__init__(doctor)
        self.specialization = doctor["specialization"]
        self.workHoures = doctor["workHoures"]

    def getSpecialization(self):
        return self.specialization

    def getWorkHour(self):
        return self.workHoures