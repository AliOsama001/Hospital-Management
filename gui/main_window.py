import streamlit as st
from data import User_repo

class Main_window:
    def __init__(self):
        options = ["Login", "Register"]
        chosen = st.sidebar.radio("Choose option: ", options)
        if chosen == options[0]:
            self.login()
        elif chosen == options[1]:
            self.register()

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
                st.session_state.users = User_repo()
                if st.session_state.users.isExist(id):
                    st.error("Your ID is already Exist")
                else:
                    st.session_state.users.saveUser(id, password, name, age, phone)
                    st.success("The account was successfully created.")