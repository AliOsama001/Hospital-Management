import streamlit as st
from services import Patient_service

if 'patientService' not in st.session_state:
    st.session_state.patientService = Patient_service(int(st.session_state.id))

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