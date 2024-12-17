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
    return render_template("/login.html")

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
        return redirect("/") #?userCreated=true
    return redirect("/") #?userCreated=false


@app.route("/login", methods = ['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')
    user = get_user(username, password)
    if user:
        session['user_id'] = user[0]
        session['user_prenom'] = user[1]
        session['user_points'] = user[5]
        return redirect("/accueil")
    return redirect("/login") #?Error=true -> msg d'erreur

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

@app.get("/information")
def information():
    if session:
        return render_template('information.html', nom=session['user_prenom'], points=session['user_points'], log='Logout')
    return render_template('information.html', nom='Invité', points='0', log='Login')

@app.get("/classement")
def classement():
    if session:
        return render_template('classement.html', nom=session['user_prenom'], points=session['user_points'], log='Logout')
    return render_template('classement.html', nom='Invité', points='0', log='Login')

@app.get("/accueil")
def accueil():
    if session:
        return render_template('accueil.html', nom=session['user_prenom'], points=session['user_points'], log='Logout')
    return render_template('accueil.html', nom='Invité', points='0', log='Login')

@app.get("/quiz")
@login_required
def quiz():
    if session:
        return render_template('quiz.html', nom=session['user_prenom'], points=session['user_points'], log='Logout')
    return render_template('quiz.html', nom='Invité', points='0', log='Login')

@app.get("/register")
def register():
    return render_template('register.html')

@app.get("/paris")
@login_required
def paris():
    if session:
        return render_template('paris.html', nom=session['user_prenom'], points=session['user_points'], log='Logout')
    return render_template('paris.html', nom='Invité', points='0', log='Login')