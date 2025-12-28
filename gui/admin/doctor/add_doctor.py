from services import Administrator_service
import streamlit as st

if "administratorService" not in st.session_state:
    st.session_state.administratorService = Administrator_service()

st.title("Add Doctor")

left, right = st.columns(2)
with left:
    id = st.text_input("Enter doctor ID")
    password = st.text_input("Enter password", type="password")
    name = st.text_input("Enter doctor name")
with right:
    specialization = st.text_input("Enter specialization")
    workHours = st.text_input("Enter work Hours e.g (hh:mm:ss)")
    phone = st.text_input("Enter doctor phone")
if st.button("Add Doctor"):
    result = st.session_state.administratorService.add_doctor(int(id), name,password, phone, specialization, workHours)
    if result: 
        st.success("Doctor added successfully")
    else:
        st.error("Can not add Doctor")