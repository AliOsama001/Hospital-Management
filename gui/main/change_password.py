import streamlit as st
from services import User_service

st.title("Change Password")

old_password = st.text_input("Old Password", type="password")
new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm New Password", type="password")

if st.button("Change Password"):
    if new_password != confirm_password:
        st.error("New passwords do not match.")
    else:
        user = User_service()
        if not user.verifyPassword(st.session_state.id, old_password):
            st.error("Old password is incorrect.")
        else:
            changed = user.changePassword(st.session_state.id, new_password)
            if not changed:
                st.error("Failed to change password.")
            else:
                st.success("Password changed successfully.")