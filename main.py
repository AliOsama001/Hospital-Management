from gui import *
import streamlit as st

st.set_page_config(
    page_title="Hopital Management",
    page_icon="assets/hospital.png",
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

if "id" not in st.session_state:
    st.session_state.id = 0

if st.session_state.page == "login":
    st.session_state.user = Main_window()
elif st.session_state.page == "patient":
        st.session_state.user = Patient_window()
elif st.session_state.page == "doctor":
        st.session_state.user = Doctor_window()
elif st.session_state.page == "administrator":
        st.session_state.user = Administrator_window()