import hashlib
import sqlite3
from flask import Flask, redirect, render_template, request, session, url_for

from database.database import create_database, create_user, get_user
from decorator.auth import login_required



    
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