import streamlit as st
from data import User_repo

class Main_window:
    def __init__(self):
        options = ["Login", "Register", "Forget Password"]
        chosen = st.sidebar.radio("Choose option: ", options)
        if chosen == options[0]:
            self.login()
        elif chosen == options[1]:
            self.register()
        elif chosen == options[2]:
            self.forget_password()

    def login(self):
        left, mid,right = st.columns([6, 1, 4])
        with left:
            st.space("large")
            st.title("Login Page")
            with st.form("login Form"):
                id = st.text_input("ID")
                password = st.text_input("Password", type="password")
                if st.form_submit_button("Login"):
                    st.session_state.userRepo = User_repo()
                    users = st.session_state.userRepo.loadUsers()
                    if id in users and users[id]["password"] == password:
                        st.session_state.id = id
                        st.session_state.loggedIn = True
                        st.session_state.page = users[id]["role"]
                        st.success("🎉 Login successful!")
                    else :
                        st.session_state.loggedIn = False
                        st.session_state.page = "login"
                        st.session_state.id = ""
                        st.error("Wrong ID or Password")
        with right:
            st.space("large")
            st.space("large")
            st.image("assets/medical-team.png", width=300)

    def register(self):
        # TODO do register function
        st.info("Register functionality coming soon.")

    def forget_password(self):
        # TODO do forget password function
        st.info("Forget Password functionality coming soon.")