from .person import Person

class Doctor(Person):
    def __init__(self, doctor:dict):
        super().__init__(doctor)
        self.specialization = doctor["specialization"][0]
        self.workHoures = doctor["workHoures"][0]

    def getSpecialization(self):
        return self.specialization

    def getWorkHour(self):
        return self.workHoures