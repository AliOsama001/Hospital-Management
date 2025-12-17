from config import ADMINISTRATOR_CSV
import pandas as pd

class Administrator_repo:
    def __init__(self):
        self.admins = pd.read_csv(ADMINISTRATOR_CSV)