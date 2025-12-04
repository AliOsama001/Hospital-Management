import streamlit as st
from data import User_repo

class Main_window:
    def login(self):
        st.title("Login Page")
        id = st.text_input("ID")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = User_repo()
            users = user.loadUsers()
            if id in users and users[id]["password"] == password:
                st.session_state.id = id
                st.session_state.role = users[id]["role"]
                st.session_state.loggedIn = True
                st.success("🎉 Login successful!")
            else :
                st.session_state.loggedIn = False
                st.session_state.role = ""
                st.session_state.id = ""
                st.error("Wrong ID or Password")

    def register(self):
        st.title("Register")