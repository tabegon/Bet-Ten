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
    db.execute('''CREATE TABLE IF NOT EXISTS joueurs (
               id INTEGER PRIMARY KEY,
               nom_complet TEXT NOT NULL,
               fichier_html TEXT NOT NULL
               )''')
    db.commit()
    joueurs = [
        (1, 'Alexander Zverev', 'static/joueurs/alexander_zverev.html'),
        (2, 'Jannik Sinner', 'static/joueurs/jannik_sinner.html')]
    db.executemany('''INSERT OR REPLACE INTO Joueurs (id, nom_complet, fichier_html) VALUES (?, ?, ?)''', joueurs)
    db.commit()
    db.close()


def get_user(username):
    db = get_db()
    result = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    db.close()
    return result

def create_user(prenom, nom, username, password):
    db = get_db()
    db.execute(f'''INSERT INTO users (prenom, nom, username, password, points)
                VALUES (?, ?, ?, ?, 100);''', (prenom, nom, username, password))
    db.commit()
    db.close()


def get_joueurs():
    db = get_db()
    result = db.execute('SELECT * FROM joueurs').fetchall()
    db.close()
    return result

def get_joueur(joueur_id):
    db = get_db()
    result = db.execute('SELECT * FROM joueurs WHERE id = ?', (joueur_id,)).fetchone()
    db.close()
    return result