import streamlit as st
from login import login_system
from client_interface import run_client_interface
from agent_dashboard import run_agent_dashboard

def main():
    st.set_page_config(page_title="Simulation Prêt", layout="wide")

    user, role = login_system()

    if user:
        st.sidebar.success(f"Connecté en tant que {user} ({role})")
        if role == "client":
            run_client_interface(user)
        elif role == "agent":
            run_agent_dashboard()

if __name__ == "__main__":
    main()
