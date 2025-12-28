import streamlit as st
from services import Doctor_service
from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return None

st.logo("assets/doctor.png")
st.session_state.doctorService = Doctor_service(int(st.session_state.id))
if st.session_state.doctorService.patientID == None:
    st.warning("No patients booked for today")
    lottie_break = load_lottiefile("assets/coffee-break.json")
    if lottie_break:
        st_lottie(lottie_break, height=600, key="break")
else:
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

    if st.button("Save & Next"):
        st.session_state.doctorService.savePatientInfo(notes, medicine, st.session_state.doctorService.pateint.getAppointment())
        next_patient = st.session_state.doctorService.nextPatient()
        st.rerun()