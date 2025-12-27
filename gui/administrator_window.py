from services import Administrator_service
import streamlit as st

class Administrator_window:
    def __init__(self):
        choice = st.sidebar.selectbox("Choose", ["edit doctor", "edit patient"])

        if choice == "edit doctor":
            st.header("Doctor Management")
            action = st.selectbox("Action", ["Add Doctor", "Delete Doctor"])

            if action == "Add Doctor":
                left, right = st.columns(2)

                with left:
                    id = st.text_input("Enter doctor ID")
                    name = st.text_input("Enter doctor name")
                    phone = st.text_input("Enter doctor phone")

                with right:
                    specialization = st.text_input("Enter specialization")
                    workHours = st.text_input("Enter work hours (e.g., 09:00:00)")

                if st.button("Add Doctor"):
                    doctor = Administrator_service()
                    result = doctor.add_doctor(int(id), name, phone, specialization, workHours)
                    st.success(result)

            elif action == "Delete Doctor":
                id = st.text_input("Enter doctor ID to delete")

                if st.button("Delete Doctor"):
                    doctor = Administrator_service()
                    result = doctor.delete_doctor(int(id))

                    if result is False:
                        st.error(f"Doctor ID {id} not found")
                    else:
                        st.success(f"Doctor ID {id} deleted successfully")

        elif choice == "edit patient":
            st.header("Patient Management")
            action = st.selectbox("Action", ["Add Patient", "Delete Patient"])

            if action == "Add Patient":
                left, right = st.columns(2)

                with left:
                    id = st.text_input("Enter patient ID")
                    name = st.text_input("Enter patient name")

                with right:
                    phone = st.text_input("Enter patient phone")

                if st.button("Add Patient"):
                    patient = Administrator_service()
                    result = patient.add_patient(id, name, phone)
                    st.success(result)

            elif action == "Delete Patient":
                id =  st.text_input("Enter patient ID to delete")

                if st.button("Delete Patient"):
                    patient = Administrator_service()
                    result = patient.delete_patient(int(id))

                    if result is False:
                        st.error(f"Patient ID {id} not found")
                    else:
                        st.success(f"Patient ID {id} deleted successfully")