from .administrator_window import Administrator_window
from .doctor_window import Doctor_window
from .patient_window import Patient_window
from .pharmaceutical_window import Pharmaceutical_window
from services import *
import streamlit as st

class Main_window:
    def __init__(self):
        self.agents = ["Patient", "Doctor", "Pharmaceutical", "Admin"]
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        
        if not st.session_state.logged_in:
            self.login_page()
        else:
            self.dashBoard()


    def login_page(self):
        st.sidebar.image("assets/hospital.png", width=100)
        chosen = st.sidebar.radio(
            "Who are You ?",
            self.agents
        )
        if chosen == self.agents[0]:
            self.patient_login()
        elif chosen == self.agents[1]:
            self.dector_login()
        elif chosen == self.agents[2]:
            self.pharmaceutical_login()
        elif chosen == self.agents[3]:
            self.admin_login()


    def patient_login(self):
        st.image("assets/patient.png", width=150)
        st.title("Welcome to Patient login")
        id = st.text_input("Your ID")
        password = st.text_input("Your Password")
        if st.button("Login"):
            patient = Patient_service()
            st.session_state.logged_in = patient.login(id, password)
            st.session_state.agent=self.agents[0]
            if st.session_state.logged_in:
                st.success("Login Successful")
            else:
                st.error("Wrong Email or Password")
            st.rerun()


    def dector_login(self):
        st.image("assets/doctor.png", width=150)
        st.title("Dont play here, we are working!!")


    def pharmaceutical_login(self):
        st.image("assets/pharmaceutical.png", width=150)
        st.title("Dont play here, we are working!!")



    def admin_login(self):
        st.image("assets/admin.png", width=150)
        st.title("Dont play here, we are working!!")


    def dashBoard(self):
        if st.session_state.agent == self.agents[0]:
            patient_win = Patient_window()
        elif st.session_state.agent == self.agents[1]:
            doctor_win = Doctor_window()
        elif st.session_state.agent == self.agents[2]:
            pharm_win = Pharmaceutical_window()
        elif st.session_state.agent == self.agents[3]:
            admin_win = Administrator_window()