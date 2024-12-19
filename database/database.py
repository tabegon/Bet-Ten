import hashlib
import sqlite3


def get_user(username, password):
    conn = sqlite3.connect('tennis.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    conn.commit()
    result = c.fetchone()
    conn.close()
    if not result:
        return None
    if result[4] == hashlib.md5(password.encode()).hexdigest():
        return result
    return None

def create_database():
    conn = sqlite3.connect('tennis.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT, 
              prenom VARCHAR(50),
              nom VARCHAR(100),
              username VARCHAR(50) UNIQUE,
              password VARCHAR(255),
              points INTEGER 
               )''')
    conn.commit()
    conn.close()

def create_user(prenom, nom, username, password):
    conn = sqlite3.connect('tennis.db')
    c = conn.cursor()
    c.execute(f'''INSERT INTO users (prenom, nom, username, password, points)
                VALUES (?, ?, ?, ?, 100);''', (prenom, nom, username, password))
    conn.commit()
    conn.close()