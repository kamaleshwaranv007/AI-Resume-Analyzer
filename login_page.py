import streamlit as st

# ============================================
# STEP 1: Define allowed users here
# (username: password) - change these to your own
# ============================================
USERS = {
    "KAMALESHWARAN":"Kamal007",
}

def login_page():
    """Shows a login form. Returns True if login is successful."""

    st.title("🔐 Login")
    st.write("Please log in to access the AI Resume Analyzer")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.rerun()  # reload the page so the main app shows
        else:
            st.error("❌ Invalid username or password")

    return False


def check_login():
    """
    Call this at the very top of your app.py, before any other code.
    If the user is not logged in, it shows the login page and stops
    the rest of the app from running.
    """

    # Create the session state key the first time the app runs
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login_page()
        st.stop()  # stops the rest of app.py from running


# ============================================
# Optional: Logout button
# Call this anywhere you want a logout option
# (e.g. in the sidebar of your main app)
# ============================================
def logout_button():
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()
      
