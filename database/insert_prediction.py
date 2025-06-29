import sqlite3
from datetime import datetime

def insert_prediction(name, features, result):
    conn = sqlite3.connect("database/predictions.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            features TEXT,
            result TEXT,
            timestamp TEXT
        )
    ''')

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO predictions (name, features, result, timestamp) VALUES (?, ?, ?, ?)",
                   (name, str(features), result, timestamp))
    conn.commit()
    conn.close()
