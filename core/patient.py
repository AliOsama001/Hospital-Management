class Patient:
    def __init__(self, index:int, users:dict):
        self.id = users["id"][index]
        self.password = users["password"][index]
        self.name = users["name"][index]
        self.age = users["age"][index]
        self.phone = users["phone"][index]
        self.notes = users["notes"][index]
        self.medicines = users["medicines"][index]
        self.date = users["date"][index]
        self.doctor = users["doctor"][index]