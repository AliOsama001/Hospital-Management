from services import Administrator_service
import streamlit as st


left, right = st.columns(2)
with left:
    id = st.text_input("Enter patient ID")
    name = st.text_input("Enter patient name")
with right:
    phone = st.text_input("Enter patient phone")
    if st.button("Add Patient"):
        patient = Administrator_service()
        result = patient.add_patient(id, name, phone)
        st.success(result)