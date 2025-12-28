from services import Administrator_service
import streamlit as st

if "administratorService" not in st.session_state:
    st.session_state.administratorService = Administrator_service()

st.logo("assets/admin.png")
st.title("Delete Patient")

id =  st.text_input("Enter patient ID to delete")
if st.button("Delete Patient"):
    result = st.session_state.administratorService.delete_patient(int(id))
    if result:
        st.success(f"Patient ID {id} deleted successfully")
    else:
        st.error(f"Patient ID {id} not found")