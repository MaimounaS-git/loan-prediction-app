import streamlit as st

def run_client_interface(username):
    st.title("Simulation de prêt")
    st.write(f"Bienvenue, {username} !")

    # Exemple de formulaire
    montant = st.number_input("Montant du prêt", min_value=1000, step=1000)
    revenu = st.number_input("Revenu mensuel", min_value=0)
    age = st.slider("Âge", 18, 70)

    if st.button("Simuler"):
        st.success("Simulation réussie ! (modèle à intégrer)")
