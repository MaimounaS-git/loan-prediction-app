import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib

# Charger les données
df = pd.read_csv("model/UCI_Credit_Card.csv")

# Features utilisées
features = ["LIMIT_BAL", "EDUCATION", "AGE", "BILL_AMT1", "PAY_AMT1"]
X = df[features]
y = df["default.payment.next.month"]

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Modèle
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Évaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Sauvegarde
joblib.dump(model, "model/predict_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
