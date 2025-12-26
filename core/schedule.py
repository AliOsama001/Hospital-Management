class Schedule:
    def __init__(self, id, schedule):
        self.id = id
        self.specialization = schedule["specialization"]
        self.doctorName = schedule["doctorName"]
        self.date = schedule["date"]

    def getSpecialization(self):
        return self.specialization

    def setSpecialization(self, specialization):
        self.specialization = specialization

    def getDoctor(self):
        return self.doctorName

    def setDoctor(self, doctorName):
        self.doctorName = doctorName

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date