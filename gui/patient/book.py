import streamlit as st
from services import Patient_service

if 'patientService' not in st.session_state:
    st.session_state.patientService = Patient_service(int(st.session_state.id))

st.logo("assets/patient.png")

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