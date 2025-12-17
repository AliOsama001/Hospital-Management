class Person:
    def __init__(self, person:dict):
        self.id = person["id"]
        self.name = person["name"]
        self.phone = person["phone"]

    def getName(self):
        return self.name

    def getPhone(self):
        return self.getPhone