from services import Doctor_service
from utils import logout
import streamlit as st

class Doctor_window:
    def __init__(self):
        st.logo("assets/doctor.png")
        st.session_state.doctorService = Doctor_service(int(st.session_state.id))
        st.title("Doctor Dashboard")
        st.divider()
        Left, right = st.columns(2)
        with Left:
            with st.container(border=True):
                st.markdown("**Doctor**: "+ str(st.session_state.doctorService.doctor.getName()))
                st.markdown("**Specialization**: "+ str(st.session_state.doctorService.doctor.getSpecialization()))
                st.markdown("**Date**: "+ str(st.session_state.doctorService.pateint.getDate()))
                st.markdown("**Phone**: 0"+ str(st.session_state.doctorService.doctor.getPhone()))
                st.space("medium")
        with right:
            with st.container(border=True):
                st.markdown("**Name**: "+ str(st.session_state.doctorService.pateint.getName()))
                st.markdown("**Age**: "+ str(st.session_state.doctorService.pateint.getAge()))
                st.markdown("**Phone**: 0"+ str(st.session_state.doctorService.pateint.getPhone()))
                st.date_input("Next Appointment:", min_value="today")
        with st.container(border=True):
            st.subheader("Visit Information")
            medicine = st.text_area("Medicine", str(st.session_state.doctorService.pateint.getMedicine()))
            notes = st.text_area("Notes", str(st.session_state.doctorService.pateint.getNotes()))
        col1, col2 = st.columns([6,1])
        with col1:
            if st.button("Logout"):
                logout()
        with col2:
            if st.button("Save & Next"):
                st.session_state.doctorService.savePatientInfo(notes, medicine, st.session_state.doctorService.pateint.getAppointment())
                next_patient = st.session_state.doctorService.nextPatient()
                if next_patient is None:
                    st.warning("No more patients for today")
                else:
                    st.rerun()