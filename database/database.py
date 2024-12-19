import hashlib
import sqlite3


def get_db():
    db = sqlite3.connect('tennis.db')
    db.row_factory = sqlite3.Row
    return db


def create_database():
    db = get_db()
    db.execute('''CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT, 
              prenom VARCHAR(50),
              nom VARCHAR(100),
              username VARCHAR(50) UNIQUE,
              password VARCHAR(255),
              points INTEGER 
               )''')
    db.commit()
    db.close()


def get_user(username):
    db = get_db()
    result = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    db.close()
    if not result:
        return None
    return result

def create_user(prenom, nom, username, password):
    db = get_db()
    db.execute(f'''INSERT INTO users (prenom, nom, username, password, points)
                VALUES (?, ?, ?, ?, 100);''', (prenom, nom, username, password))
    db.commit()
    db.close()