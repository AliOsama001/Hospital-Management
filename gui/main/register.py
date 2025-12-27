import streamlit as st
from services import User_service

st.space("large")
st.title("Register Page")
with st.form("Register Form"):
    left, right = st.columns(2)
    with left:
        name = st.text_input("Your Name:")
        age = st.number_input("Your Age:", step=1, min_value=0, max_value=100)
        phone = st.text_input("Your Phone:")
    with right:
        id = st.text_input("Your ID")
        password = st.text_input("Your Password", type="password")
    if st.form_submit_button("Submit"):
        userService = User_service()
        if userService.regiter(id, password, name, age, phone):
            st.success("Your account has been created successfully")
        else:
            st.error("This ID is already registered")