ample app showing how to login import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(page_title="SecureApp", page_icon="🔑", layout="wide")

# -------------------------------
# Initialize session state
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "main"

# -------------------------------
# Helper to safely check login
# -------------------------------
def is_logged_in():
    return hasattr(st, "user") and hasattr(st.user, "is_logged_in") and st.user.is_logged_in

# -------------------------------
# Main page
# -------------------------------
def main():
    if not is_logged_in():
        st.title("An example Streamlit app showing how to use OIDC to authorize logging in via Google email.")
        st.subheader("Use the Login button on the left hand menu block")
    else:
        st.title("Congratulations")
        st.subheader("You have successfully logged in! You can now click on the Dashboard button link.")

# -------------------------------
# Dashboard page
# -------------------------------
def dashboard():
    st.title("Dashboard")
    user_name = st.user.name if is_logged_in() else "Guest"
    st.subheader(f"Welcome, {user_name}!")

    # Dummy Data
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": np.random.randint(100, 500, 6),
        "Profit": np.random.randint(20, 100, 6)
    })

    # Display DataFrame
    st.dataframe(df)

    # Line Chart for Sales
    fig1, ax1 = plt.subplots()
    ax1.plot(df["Month"], df["Sales"], marker="o", linestyle="-", label="Sales")
    ax1.set_title("Monthly Sales Trend")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Sales")
    ax1.legend()
    st.pyplot(fig1)

    # Bar Chart for Profit
    fig2, ax2 = plt.subplots()
    ax2.bar(df["Month"], df["Profit"], color="green", label="Profit")
    ax2.set_title("Monthly Profit")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Profit")
    ax2.legend()
    st.pyplot(fig2)

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.header("Navigation")

# Determine label for login/logout button
sidebar_button_label = "Logout" if is_logged_in() else "Login"

# Login/Logout logic
if st.sidebar.button(sidebar_button_label):
    if is_logged_in():
        st.logout()
        st.session_state.page = "main"
        st.rerun()
    else:
        st.login("google")  # Or another provider name you configured in secrets.toml

# Dashboard link button (enabled only when logged in)
if st.sidebar.button("Dashboard", disabled=not is_logged_in()):
    st.session_state.page = "dashboard"
    st.rerun()

# -------------------------------
# Page Rendering
# -------------------------------
if st.session_state.page == "main":
    main()
elif st.session_state.page == "dashboard":
    dashboard()
