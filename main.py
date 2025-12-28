import streamlit as st

st.logo("assets/hospital.png")

if "role" not in st.session_state:
    st.session_state.role = None
if "id" not in st.session_state:
    st.session_state.id = 0

role = st.session_state.role

logout_page = st.Page("gui/main/logout.py", title="Logout", icon=":material/logout:")
change_password_page = st.Page("gui/main/change_password.py", title="Change Password", icon=":material/settings:")
book_patinent_page = st.Page("gui/patient/book.py", title="Book Appointment", default=(role == "patient"))
delete_appointment_page = st.Page("gui/patient/delete.py", title="Delete Appointment")
view_appointments_page = st.Page("gui/patient/view.py", title="View Appointments")
dashboard_page = st.Page("gui/doctor/dashboard.py", title="Dashboard", default=(role == "doctor"))
add_doctor_page = st.Page("gui/admin/doctor/add_doctor.py", title="Add Doctor", icon=":material/person_add:", default=(role == "administrator"))
remove_doctor_page = st.Page("gui/admin/doctor/delete_doctor.py", title="Remove Doctor", icon=":material/person_remove:")
add_patient_page = st.Page("gui/admin/patient/add_patient.py", title="Add Patient", icon=":material/person_add:")
remove_patient_page = st.Page("gui/admin/patient/delete_patient.py", title="Remove Patient", icon=":material/person_remove:")
login = st.Page("gui/main/login.py", title="Login", icon= ":material/login:")
register = st.Page("gui/main/register.py", title="Register", icon=":material/app_registration:")

account_pages = [logout_page, change_password_page]
patient_pages = [book_patinent_page, delete_appointment_page, view_appointments_page]
doctor_pages = [dashboard_page]
administrator_doctor_pages = [add_doctor_page, remove_doctor_page]
administrator_patient_pages = [add_patient_page, remove_patient_page]
main_pages = [login, register]

page_dict = {}

if st.session_state.role == "patient":
    page_dict["Patient"] = patient_pages
if st.session_state.role == "doctor":
    page_dict["Doctor"] = doctor_pages
if st.session_state.role == "administrator":
    page_dict["Doctor Management"] = administrator_doctor_pages
    page_dict["Patient Management"] = administrator_patient_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation({"Main": main_pages})
pg.run()