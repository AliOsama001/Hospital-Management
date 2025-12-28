from config import DOCTOR_CSV, PATIENT_CSV
import pandas as pd

class Administrator_repo:
    def __init__(self):
        self.docs = pd.read_csv(DOCTOR_CSV)
        self.pats = pd.read_csv(PATIENT_CSV)