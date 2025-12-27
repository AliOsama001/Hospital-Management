from services import Administrator_service
import streamlit as st

left, right = st.columns(2)
with left:
    id = st.text_input("Enter doctor ID")
    name = st.text_input("Enter doctor name")
    phone = st.text_input("Enter doctor phone")
with right:
    specialization = st.text_input("Enter specialization")
    workHours = st.text_input("Enter work hours (e.g., 09:00:00)")
if st.button("Add Doctor"):
    doctor = Administrator_service()
    result = doctor.add_doctor(int(id), name, phone, specialization, workHours)
    st.success(result)