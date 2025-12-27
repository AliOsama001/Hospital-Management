from config import SCHEDULE_JSON
import json

class Schedule_repo:
    def __init__(self):
        try:
            with open(SCHEDULE_JSON, "r") as f:
                self.schedule = json.load(f)
        except:
            self.schedule = {}

    def nextPatient(self, specialization):
        if len(self.schedule) == 0:
            return None
        for i in self.schedule:
            if self.schedule[i]["specialization"] == specialization:
                return i, self.schedule[i]

    def addBook(self, patientID, specialization, doctor, date):
        self.schedule[patientID] = {
            "specialization": specialization,
            "doctorName": doctor,
            "date": date
        }

    def deleteBook(self, patientID):
        if patientID in self.schedule:
            del self.schedule[patientID]

    def getSchedule(self, id):
        try:
            return self.schedule[str(id)]
        except:
            return None

    def isBooked(self, id):
        return id in self.schedule

    def saveChanges(self):
        with open(SCHEDULE_JSON, "w") as f:
            json.dump(self.schedule, f)