import streamlit as st
from streamlit_lottie import st_lottie
import json
from time import sleep
from services import User_service

def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return None

left, mid,right = st.columns([6,1,5])
with left:
    st.space("large")
    st.title("Login Page")
    with st.form("login Form"):
        id = st.text_input("ID")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            userService = User_service()
            role = userService.login(id, password)
            if role != None:
                st.session_state.id = id
                st.session_state.role = role
                st.success("Signed in Successfully")
                sleep(1)
                st.rerun()
            else:
                st.session_state.id = 0
                st.session_state.role = None
                st.error("Invalid ID or Password")
with right:
    st.space("medium")
    lottie_doctor = load_lottiefile("assets/Doctor.json")
    if lottie_doctor:
        st_lottie(lottie_doctor, height=500, key="login_doc")