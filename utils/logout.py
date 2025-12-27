import streamlit as st

def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.id = 0
    st.rerun()