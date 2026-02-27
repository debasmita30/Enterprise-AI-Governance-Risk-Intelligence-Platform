import streamlit as st
import bcrypt
import os

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

def get_users():
    return {
        os.getenv("ADMIN_USER", "admin"):
            hash_password(os.getenv("ADMIN_PASS", "admin123")),
        os.getenv("ANALYST_USER", "analyst"):
            hash_password(os.getenv("ANALYST_PASS", "analyst123")),
        os.getenv("VIEWER_USER", "viewer"):
            hash_password(os.getenv("VIEWER_PASS", "viewer123"))
    }

def login_page():
    st.title("Enterprise AI Governance Platform")
    st.subheader("Secure Login")

    users = get_users()

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and check_password(password, users[username]):
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

    if st.button("Load Demo Access"):
        st.session_state.authenticated = True
        st.session_state.user = "admin"
        st.rerun()

def require_auth():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if not st.session_state.authenticated:
        login_page()
        st.stop()

def logout():
    st.session_state.authenticated = False
    st.session_state.clear()
    st.rerun()