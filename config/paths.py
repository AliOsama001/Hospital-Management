import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_DIR = os.path.join(DATA_DIR, "csv")
JSON_DIR = os.path.join(DATA_DIR, "json")

ADMINISTRATOR_CSV = os.path.join(CSV_DIR, "administrator.csv")
DOCTOR_CSV = os.path.join(CSV_DIR, "doctor.csv")
PATIENT_CSV = os.path.join(CSV_DIR, "patient.csv")
USER_JSON = os.path.join(JSON_DIR, "user.json")
SCHEDULE_JSON = os.path.join(JSON_DIR, "schedule.json")

os.makedirs(CSV_DIR, exist_ok=True)