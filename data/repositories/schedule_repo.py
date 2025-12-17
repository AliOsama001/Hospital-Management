from config import SCHEDULE_JSON
import json

class Schedule_repo:
    def __init__(self):
        try:
            with open(SCHEDULE_JSON, "r") as f:
                self.schedule = json.load(f)
        except:
            self.schedule = {}