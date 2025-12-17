from services import User_service
import streamlit as st

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
                    userService = User_service()
                    page = userService.login(id, password)
                    if page != "":
                        st.session_state.logged_in = True
                        st.session_state.id = id
                        st.session_state.page = page
                        st.success("Signed in Successfully")
                        st.rerun()
                    else:
                        st.session_state.logged_in = False
                        st.session_state.id = 0
                        st.session_state.page = "login"
                        st.error("Invalid ID or Password")
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
                userService = User_service()
                if userService.regiter(id, password, name, age, phone):
                    st.success("Your account has been created successfully")
                else :
                    st.error("This ID is already registered")