import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_DIR = os.path.join(DATA_DIR, "csv")

ADMINISTRATOR_DIR = os.path.join(CSV_DIR, "administrator")
DOCTOR_DIR = os.path.join(CSV_DIR, "doctor")
PATIENT_DIR = os.path.join(CSV_DIR, "patient")
PHARMACEUTICAL_DIR = os.path.join(CSV_DIR, "pharmaceutical")

os.makedirs(CSV_DIR, exist_ok=True)