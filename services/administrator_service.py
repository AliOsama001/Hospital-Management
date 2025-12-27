import pandas as pd
import json
from config import PATIENT_CSV, DOCTOR_CSV
doctor_file=DOCTOR_CSV
patient_file=PATIENT_CSV

def read(path_file):
    return pd.read_csv(path_file)
def save_csv(df, path_file):
    df.to_csv(path_file, index=False)

class Administrator_service:
    def __init__(self):
        pass
    
    def add_doctor(self, id, name, phone, specialization, workHours):
            df = read(doctor_file)

            if id in df["id"].values:
                return f"Error: ID {id} already exists"

            new_doctor = pd.DataFrame([{
                "id": id,
                "name": name,
                "phone": phone,
                "specialization": specialization,
                "workHours": workHours
            }])

            df = pd.concat([df, new_doctor], ignore_index=True)

            save_csv(df, doctor_file)

            return f"Doctor added successfully with ID: {id}"

    def delete_doctor(self, id):
        df = read(doctor_file)

        if id not in df["id"].values:
            return False

        df = df[df["id"] != id]

        save_csv(df, doctor_file)

        return True


    def add_patient(self, id, name, phone):
        df = read(patient_file)

        if id in df["id"].values:
            return f"Error: ID {id} already exists"

        new_patient = pd.DataFrame([{
            "id": id,
            "name": name,
            "phone": phone
        }])

        df = pd.concat([df, new_patient], ignore_index=True)

        save_csv(df, patient_file)

        return f"Patient added successfully with ID: {id}"


    def delete_patient(self, id):
            df = read(patient_file)

            if id not in df["id"].values:
                return False

            df = df[df["id"] != id]

            save_csv(df, patient_file)

            return True
