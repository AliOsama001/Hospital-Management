from services import Patient_service
from utils import logout
import streamlit as st

class Patient_window:
    def __init__(self):
        st.logo("assets/patient.png")
        st.session_state.patientService = Patient_service(int(st.session_state.id))
        patient_options = ["Book an appointment", "Delete an appointment", "Show Prescription"]
        patient_chosen = st.sidebar.radio("Choose Option:", patient_options)
        if patient_chosen == patient_options[0]:
            self.book()
        elif patient_chosen == patient_options[1]:
            self.edit()
        elif patient_chosen == patient_options[2]:
            self.show()
        st.sidebar.divider()
        if st.sidebar.button("logout"):
            logout()

    def book(self):
        st.title("Book an Appointment")
        specializations = st.session_state.patientService.getSpecializations()
        specialization = st.selectbox("Choose Specialization:", specializations)
        doctors = st.session_state.patientService.getDoctors(specialization)
        doctorName = st.selectbox("Choose Doctor:", doctors)
        date = st.date_input("Choose Date:", min_value="today")
        if st.button("Book"):
            if st.session_state.patientService.bookSchedule(specialization, doctorName, str(date)):
                st.success("Booking Successful")
            else:
                st.error("You already have a booking")

    def edit(self):
        st.title("Edit an Appointment")
        nextAppointment = st.session_state.patientService.patient.getAppointment()
        if nextAppointment == "":
            st.write("You Do not have appointment")
        else:
            st.markdown("**Specialization**: "+ st.session_state.patientService.schedule.getSpecialization())
            st.markdown("**Doctor**: "+ st.session_state.patientService.schedule.getDoctor())
            st.markdown("**Date**: "+ st.session_state.patientService.schedule.getDate())
            if st.button("Delete Appointment"):
                st.session_state.patientService.deleteSchedule()
                st.success("Appointment Deleted")

    def show(self):
        st.title("Prescription")
        st.divider()
        left, right = st.columns(2)
        with left :
            with st.container(border=True):
                st.markdown("**Dr**: "+ str(st.session_state.patientService.patient.getDoctor()))
                st.markdown("**Dr Phone**: 0"+ str(st.session_state.patientService.patient.getDoctorPhone()))
                st.markdown("**Specialization**: "+ str(st.session_state.patientService.patient.getSpecialization()))
                st.markdown("**Date**: "+ str(st.session_state.patientService.patient.getDate()))
        with right :
            with st.container(border=True):
                st.markdown("**Name**: "+ str(st.session_state.patientService.patient.getName()))
                st.markdown("**Phone**: 0"+ str(st.session_state.patientService.patient.getPhone()))
                st.markdown("**Age**: "+ str(st.session_state.patientService.patient.getAge()))
                st.markdown("**Next Appointment**: "+ str(st.session_state.patientService.patient.getAppointment()))
        with st.container(border=True):
                st.markdown("**Medicine**:")
                st.write("    ",st.session_state.patientService.patient.getMedicine())
                st.space("large")
                st.markdown("**Notes**:")
                st.write("    ",st.session_state.patientService.patient.getNotes())