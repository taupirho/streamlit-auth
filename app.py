import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="SecureApp", page_icon="🔑", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "main"

# ——— Helpers ———
def _user_obj():
    return getattr(st, "user", None)

def user_is_logged_in() -> bool:
    u = _user_obj()
    return bool(getattr(u, "is_logged_in", False)) if u else False

def user_name() -> str:
    u = _user_obj()
    return getattr(u, "name", "Guest") if u else "Guest"

# ——— Pages ———
def main():
    if not user_is_logged_in():
        st.title("An example Streamlit app showing the use of OIDC and Google email for login authentication")
        st.subheader("Use the sidebar button to log in.")
    else:
        st.title("Congratulations")
        st.subheader("You’re logged in! Click Dashboard on the sidebar.")

def dashboard():
    st.title("Dashboard")
    st.subheader(f"Welcome, {user_name()}!")

    df = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Sales": np.random.randint(100,500,6),
        "Profit": np.random.randint(20,100,6)
    })
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Sales"], marker="o", label="Sales")
    ax.set(xlabel="Month", ylabel="Sales", title="Monthly Sales Trend")
    ax.legend()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.bar(df["Month"], df["Profit"], label="Profit")
    ax.set(xlabel="Month", ylabel="Profit", title="Monthly Profit")
    ax.legend()
    st.pyplot(fig)

# ——— Sidebar & Navigation ———
st.sidebar.header("Navigation")

if user_is_logged_in():
    if st.sidebar.button("Logout"):
        st.logout()
        st.session_state.page = "main"
        st.rerun()
else:
    if st.sidebar.button("Login"):
        st.login("google")  # or "okta"
        st.rerun()

if st.sidebar.button("Dashboard", disabled=not user_is_logged_in()):
    st.session_state.page = "dashboard"
    st.rerun()

# ——— Dispatch ———
if st.session_state.page == "main":
    main()
else:
    dashboard()
