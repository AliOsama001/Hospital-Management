from .person import Person

class Doctor(Person):
    def __init__(self, doctor:dict):
        super().__init__(doctor)
        self.specialization = doctor["specialization"][0]
        self.workHours = doctor["workHours"][0]

    def getSpecialization(self):
        return self.specialization

    def getWorkHours(self):
        return self.workHours

    def setWorkHours(self, workHours):
        self.workHours = workHours