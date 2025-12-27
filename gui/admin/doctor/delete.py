from services import Administrator_service
import streamlit as st


id = st.text_input("Enter doctor ID to delete")
if st.button("Delete Doctor"):
    doctor = Administrator_service()
    result = doctor.delete_doctor(int(id))
    if result is False:
        st.error(f"Doctor ID {id} not found")
    else:
        st.success(f"Doctor ID {id} deleted successfully")