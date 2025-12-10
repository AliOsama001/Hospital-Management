from services import Patient_service
import streamlit as st

class Patient_window:
    def __init__(self):
            st.session_state.patientService = Patient_service(int(st.session_state.id))
            pat_options = ["Book an appointment", "Edit an appointment", "Show Prescription"]
            pat_chosen = st.sidebar.radio("Choose Option:", pat_options)
            if pat_chosen == pat_options[0]:
                self.book()
            elif pat_chosen == pat_options[1]:
                self.edit()
            elif pat_chosen == pat_options[2]:
                self.show()
            st.sidebar.space("large")
            st.sidebar.space("large")
            st.sidebar.space("large")
            st.sidebar.space("large")
            st.sidebar.space("large")
            st.sidebar.space("large")
            st.sidebar.space("large")
            if st.sidebar.button("logout"):
                st.session_state.logged_in = False
                st.session_state.page = "login"

    def book(self):
        st.title("Book an appointment")
        specialization = ["barin", "bones"]
        choose = st.selectbox("Choose Specialization:", specialization)
        if st.button("Submit"):
            if st.session_state.patientService.bookSchedule(choose):
                st.success("Booking Successful")
            else:
                st.error("You already have a booking")

    def edit(self):
        # TODO
        st.info("We are Working here!")

    def show(self):
        # TODO
        st.info("We are Working here!")