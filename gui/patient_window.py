from services import Patient_service
from utils import logout
import streamlit as st

class Patient_window:
    def __init__(self):
            st.session_state.patientService = Patient_service(int(st.session_state.id))
            patient_options = ["Book an appointment", "Edit an appointment", "Show Prescription"]
            patient_chosen = st.sidebar.radio("Choose Option:", patient_options)
            if patient_chosen == patient_options[0]:
                self.book()
            elif patient_chosen == patient_options[1]:
                self.edit()
            elif patient_chosen == patient_options[2]:
                self.show()
            if st.sidebar.button("logout"):
                logout()

    def book(self):
        # TODO
        st.info("We are Working here!")

    def edit(self):
        # TODO
        st.info("We are Working here!")

    def show(self):
        st.title("Prescription")
        left, right = st.columns(2)
        with left :
            with st.container(border=True):
                pass
        with right :
            with st.container(border=True):
                pass
        with st.container(border=True):
                pass