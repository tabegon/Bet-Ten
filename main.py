import hashlib
import sqlite3
from flask import Flask, redirect, render_template, request, session

from decorator.auth import login_required


def get_user(username, password):
    query = f'''SELECT * FROM users WHERE username = ?'''
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
    return redirect("/login.html", code=302)

@app.route("/hello")
@login_required
def hello_world():
    return f"<p>Hello, {session['user_prenom']}!</p>"

@app.route("/new_user", methods = ['POST'])
def new_user():
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    username = request.form.get('username')
    password = request.form.get('password')
    if password :
        password_cryptee = hashlib.md5(password.encode()).hexdigest()
        create_user(prenom, nom, username, password_cryptee)
        return redirect("/login.html?userCreated=true", code=302)
    return redirect("/login.html?userCreated=false", code=302)


@app.route("/login", methods = ['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')
    user = get_user(username, password)
    if user:
        session['user_id'] = user[0]
        session['user_prenom'] = user[1]
        return redirect("/main.html", code=302)
    return redirect("/login.html?Error=true", code=302)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/login.html')

@app.get("/information")
def information():
    return render_template('information.html')