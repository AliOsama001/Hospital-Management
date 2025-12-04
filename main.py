from gui import Main_window
import streamlit as st

st.set_page_config(
    page_title="Hospital Management",
    page_icon="🏥"
)

user = Main_window()
options = ["Login", "Register", "Forget Password"]


chosen = st.sidebar.radio("Choose option: ", options)

if chosen == options[0]:
    user.login()
elif chosen == options[1]:
    user.register()
elif chosen == options[2]:
    # TODO: Implement forget password functionality
    st.info("Forget Password functionality coming soon.")

if "loggedIn" in st.session_state:
    if st.session_state.role == "patient":
        st.switch_page("pages/patient_window.py")