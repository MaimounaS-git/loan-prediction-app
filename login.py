import streamlit as st

users = {
    "maimouna": {"password": "pass1", "role": "client"},
    "mansour": {"password": "pass2", "role": "agent"}
}

def login_system():
    st.sidebar.title("Connexion")

    username = st.sidebar.text_input("Nom d'utilisateur")
    password = st.sidebar.text_input("Mot de passe", type="password")

    if st.sidebar.button("Se connecter"):
        if username in users and users[username]["password"] == password:
            return username, users[username]["role"]
        else:
            st.sidebar.error("Identifiants incorrects.")
            return None, None
    return None, None
