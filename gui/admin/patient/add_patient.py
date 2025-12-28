from services import Administrator_service, User_service
import streamlit as st

if "administratorService" not in st.session_state:
    st.session_state.administratorService = Administrator_service()

st.title("Add Patient")

left, right = st.columns(2)
with left:
    name = st.text_input("Your Name:")
    age = st.number_input("Your Age:", step=1, min_value=0, max_value=100)
    phone = st.text_input("Your Phone:")
with right:
    id = st.text_input("Your ID")
    password = st.text_input("Your Password", type="password")
if st.button("Add Patient"):
    userService = User_service()
    if userService.regiter(id, password, name, phone, age):
        st.success("Your account has been created successfully")
    else:
        st.error("This ID is already registered")