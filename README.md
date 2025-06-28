# 🏦 PrêtSûr – Application de Simulation de Prêt Bancaire avec IA

PrêtSûr est une application web intelligente permettant aux clients de simuler leur éligibilité à un prêt bancaire, et aux agents bancaires de visualiser, suivre et analyser les demandes en temps réel grâce à un tableau de bord interactif.

---

## 🚀 Fonctionnalités

### 👤 Pour les clients :
- Connexion sécurisée
- Formulaire de demande de prêt
- Prédiction instantanée d’acceptation/refus via un modèle IA
- Interprétation des résultats (facteurs influents)

### 🧑🏽‍💼 Pour les agents bancaires :
- Tableau de bord avec statistiques globales
- Accès à toutes les demandes
- Visualisations interactives
- Analyse des décisions prises par l’algorithme

---

## 🧠 Technologies utilisées

| Catégorie          | Outils/Technos              |
|--------------------|-----------------------------|
| Interface          | `Streamlit`                 |
| Machine Learning   | `scikit-learn`, `joblib`    |
| Interprétation     | `SHAP`                      |
| Base de données    | `SQLite`                    |
| Conteneurisation   | `Docker`                    |
| Intégration Continue | `Jenkins` (à venir)       |
| Versioning         | `Git`, `GitHub`             |

---

## 📦 Structure du projet

loan_prediction_app/
├── app.py # Lancement principal
├── login.py # Connexion & rôles
├── client_interface.py # Interface simulation client
├── agent_dashboard.py # Interface agent bancaire
├── model/
│ └── predict_model.pkl # Modèle ML sauvegardé
├── db/
│ └── database.db # Données enregistrées
├── utils/
│ ├── db_functions.py
│ └── prediction_utils.py
├── requirements.txt
├── Dockerfile
└── README.md
