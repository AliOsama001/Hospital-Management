class Person:
    def __init__(self, person:dict):
        self.id = person["id"][0]
        self.name = person["name"][0]
        self.phone = person["phone"][0]

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone