import streamlit as st
from services import Patient_service

if 'patientService' not in st.session_state:
    st.session_state.patientService = Patient_service(int(st.session_state.id))

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