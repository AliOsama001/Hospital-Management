from core import Patient
from data import Patient_repo
import streamlit as st

class Patient_service:
    def __init__(self, id:int):
        st.session_state.patientRepo = Patient_repo()
        self.users = st.session_state.patientRepo.loadUsers()
        for user in self.users["id"]:
            if id == self.users["id"][user]:
                self.index = user
                st.session_state.patient = Patient(
                    self.users["id"][user],
                    self.users["name"][user],
                    self.users["age"][user],
                    self.users["phone"][user],
                    self.users["notes"][user],
                    self.users["medicine"][user],
                    self.users["date"][user],
                    self.users["doctor"][user]
                    )

    def getName(self):
        return st.session_state.patient.name

    def getId(self):
        return st.session_state.patient.id

    def getAge(self):
        return st.session_state.patient.age

    def getPhone(self):
        return st.session_state.patient.phone

    def editMedicine(self, newMedicine):
        st.session_state.patient.medicine = newMedicine
        self.users["medicine"][self.index] = newMedicine

    def editNotes(self, newNotes):
        st.session_state.patient.notes = newNotes
        self.users["notes"][self.index] = newNotes

    def saveChanges(self):
        st.session_state.patientRepo.saveUsers(self.users)

    def bookSchedule(self, specialization):
        return st.session_state.patientRepo.addAppointment(self.getId(), specialization)