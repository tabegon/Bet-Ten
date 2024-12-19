import hashlib
import sqlite3
from flask import Flask, redirect, render_template, request, session, url_for

from decorator.auth import login_required


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
    
create_database()
app = Flask(__name__)

app.secret_key = 'super secret key'

@app.route("/")
def index():
    return render_template("/accueil.html")



@app.get('/login')
def login():
    return render_template("/login.html")

@app.get('/register')
def register():
    return render_template('/register.html')

@app.post("/register")
def register_action():
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    username = request.form.get('username')
    password = request.form.get('password')
    if password :
        password_cryptee = hashlib.md5(password.encode()).hexdigest()
        create_user(prenom, nom, username, password_cryptee)
        return redirect(url_for('login')) #?userCreated=true
    return redirect(url_for("register")) #?userCreated=false


@app.post("/login")
def login_action():
    username = request.form.get('username')
    password = request.form.get('password')
    user = get_user(username, password)
    if user:
        session['user_id'] = user[0]
        session['user_prenom'] = user[1]
        session['user_points'] = user[5]
        return redirect(url_for('index'))
    return redirect(url_for('login')) #?Error=true -> msg d'erreur

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.get("/information")
def information():
    return render_template('information.html')

@app.get("/classement")
def classement():
    return render_template('classement.html')


@app.get("/quiz")
@login_required
def quiz():
    return render_template('quiz.html')


@app.get("/paris")
@login_required
def paris():
    return render_template('paris.html')

if __name__ == '__name__':
    app.run(host='localhost', port=5000, debug=True)