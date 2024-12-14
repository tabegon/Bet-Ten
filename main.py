import hashlib
import sqlite3
from flask import Flask, redirect, request

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
                VALUES ("{prenom}", "{nom}", "{username}", "{password}", 100);''')
    conn.commit()
    conn.close()
    
create_database()
app = Flask(__name__,
            static_url_path='',
            static_folder='app/static')


@app.route("/")
def index():
    return redirect("/login.html", code=302)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/new_user", methods = ['POST'])
def new_user():
    print(request.form.get('prenom'))
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    username = request.form.get('username')
    password = request.form.get('password')
    if password :
        password_cryptee = hashlib.md5(password.encode()).hexdigest()
        create_user(prenom, nom, username, password_cryptee)
        return redirect("/login.html?userCreated=true", code=302)
    return redirect("/login.html?userCreated=false", code=302)