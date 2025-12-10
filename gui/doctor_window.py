from services import Doctor_service
import time
import streamlit as st

class Doctor_window:
    def __init__(self):
        with st.container():
            left, right = st.columns(2)
            left.title("Dr: ")
            left.write("Name: ")
            left.write("Specialization: ")
            curr = time.ctime(time.time())
            left.write("Date: "+curr)
            right.title("Patient")
            right.write("Name: ")
            right.write("age: ")
            right.write("Phone: ")