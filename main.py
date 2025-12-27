import streamlit as st
from utils import logout, change_password

st.set_page_config(
    page_title="Hopital Management",
    page_icon="assets/hospital.png",
)

ROLES = [None, "administrator", "patient", "doctor"]

if "role" not in st.session_state:
    st.session_state.role = None
if "id" not in st.session_state:
    st.session_state.id = 0

role = st.session_state.role

logout_page = st.Page(logout, title="Logout", icon=":material/logout:")
change_password_page = st.Page(change_password, title="Change Password", icon=":material/settings:")
book_patinent_page = st.Page("gui/patient/book.py", title="Book Appointment", default=(role == "patient"))
delete_appointment_page = st.Page("gui/patient/delete.py", title="Delete Appointment")
view_appointments_page = st.Page("gui/patient/view.py", title="View Appointments")
dashboard_page = st.Page("gui/doctor/dashboard.py", title="Dashboard", default=(role == "doctor"))
add_doctor_page = st.Page("gui/admin/doctor/add.py", title="Add Doctor", icon=":material/person_add:", default=(role == "administrator"))
remove_doctor_page = st.Page("gui/admin/doctor/delete.py", title="Remove Doctor", icon=":material/person_remove:")
add_patient_page = st.Page("gui/admin/patient/add.py", title="Add Patient", icon=":material/person_add:")
remove_patient_page = st.Page("gui/admin/patient/delete.py", title="Remove Patient")
login = st.Page("gui/main/login.py", title="Login", icon= ":material/login:")
register = st.Page("gui/main/register.py", title="Register", icon=":material/app_registration:")

account_pages = [logout_page, change_password_page]
patient_pages = [book_patinent_page, delete_appointment_page, view_appointments_page]
doctor_pages = [dashboard_page]
administrator_pages = [add_doctor_page, remove_doctor_page]
main_pages = [login, register]

page_dict = {}

if st.session_state.role == "patient":
    page_dict["Patient"] = patient_pages
if st.session_state.role == "doctor":
    page_dict["Doctor"] = doctor_pages
if st.session_state.role == "administrator":
    page_dict["Administrator"] = administrator_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation({"Main": main_pages})
pg.run()