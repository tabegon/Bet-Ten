import sqlite3
from flask import Flask, redirect

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