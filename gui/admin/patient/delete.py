from services import Administrator_service
import streamlit as st

id =  st.text_input("Enter patient ID to delete")
if st.button("Delete Patient"):
    patient = Administrator_service()
    result = patient.delete_patient(int(id))
    if result is False:
        st.error(f"Patient ID {id} not found")
    else:
        st.success(f"Patient ID {id} deleted successfully")