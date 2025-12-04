import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_DIR = os.path.join(DATA_DIR, "csv")

ADMINISTRATOR_CSV = os.path.join(CSV_DIR, "administrator.csv")
DOCTOR_CSV = os.path.join(CSV_DIR, "doctor.csv")
PATIENT_CSV = os.path.join(CSV_DIR, "patient.csv")
PHARMACEUTICAL_CSV = os.path.join(CSV_DIR, "pharmaceutical.csv")
USER_FILE = os.path.join(DATA_DIR, "user.json")

os.makedirs(CSV_DIR, exist_ok=True)