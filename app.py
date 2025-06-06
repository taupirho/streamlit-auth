import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page config at the very start of the script
st.set_page_config(page_title="SecureApp", page_icon="🔑", layout="wide")

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "main"

# Function to display the main screen
def main():
    if not st.user.is_logged_in:
        st.title("Please use the button on the sidebar to login.")
    else:
        st.title("Congratulations")
        st.subheader("You have successfully logged in to the system! You can now click on the dashboard link.")

# Function to display the dashboard with dummy graphs
def dashboard():
    st.title("Dashboard")
    st.subheader(f"Welcome, {st.user.name if st.user.is_logged_in else 'Guest'}!")

    # Dummy Data
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": np.random.randint(100, 500, 6),
        "Profit": np.random.randint(20, 100, 6)
    })

    # Display Dataframe
    st.dataframe(df)

    # Line Chart for Sales
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Sales"], marker="o", linestyle="-", label="Sales")
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.legend()
    st.pyplot(fig)

    # Bar Chart for Profit
    fig, ax = plt.subplots()
    ax.bar(df["Month"], df["Profit"], color="green", label="Profit")
    ax.set_title("Monthly Profit")
    ax.set_xlabel("Month")
    ax.set_ylabel("Profit")
    ax.legend()
    st.pyplot(fig)

# Sidebar Navigation
st.sidebar.header("Navigation")

# Login/Logout Button in Sidebar
sidebar_button_label = "Logout" if st.user.is_logged_in else "Login"

if st.sidebar.button(sidebar_button_label):
    if st.user.is_logged_in:
        st.logout()
        st.session_state.page = "main"
        st.rerun()
    else:
        st.login("google")  # Change to "okta" if needed

# Sidebar Dashboard Link (Disabled if not logged in)
if st.sidebar.button("Dashboard", disabled=not st.user.is_logged_in):
    st.session_state.page = "dashboard"
    st.rerun()

# Page Navigation Logic
if st.session_state.page == "main":
    main()
elif st.session_state.page == "dashboard":
    dashboard()

