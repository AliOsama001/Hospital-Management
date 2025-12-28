from services import Administrator_service
import streamlit as st

if "administratorService" not in st.session_state:
    st.session_state.administratorService = Administrator_service()

st.logo("assets/admin.png")

st.title("Delete Doctor")
id = st.text_input("Enter doctor ID to delete")
if st.button("Delete Doctor"):
    result = st.session_state.administratorService.delete_doctor(int(id))
    if result:
        st.success(f"Doctor ID {id} deleted successfully")
    else:
        st.error(f"Doctor ID {id} not found")