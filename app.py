import hashlib
import os
import sqlite3
from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

from database.database import create_database, create_user, get_joueur, get_joueurs, get_user
from decorator.auth import login_required
from helpers import check_password, encode_password



    
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
        password_cryptee = encode_password(password)
        create_user(prenom, nom, username, password_cryptee)
        return redirect(url_for('login')) #?userCreated=true
    return redirect(url_for("register")) #?userCreated=false


@app.post("/login")
def login_action():
    username = request.form.get('username')
    password = request.form.get('password')
    user = get_user(username)
    if not user:
        flash("Nom d'utilisateur n'existe pas")
        return redirect(url_for('login'))
    if not check_password(password_bd=user['password'], input_password=password):
        flash("Password incorrect")
        return redirect(url_for('login'))
    session['user_id'] = user['id']
    session['user_prenom'] = user['prenom']
    session['user_points'] = user['points']
    return redirect(url_for('index'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.get("/forgetPassword")
def forget_password():
    return render_template('passwordinexistant.html')

@app.get("/information")
def information():
    return render_template('information.html')

@app.get("/classement")
def classement():
    joueurs = get_joueurs()
    return render_template('classement.html', joueurs=joueurs)


@app.get("/quiz")
@login_required
def quiz():
    return render_template('quiz.html')


@app.get("/paris")
@login_required
def paris():
    return render_template('paris.html')

@app.get("/paris/vosParis")
def vos_paris():
    return render_template('vos_paris.html')

@app.get("/paris/tournoisEnCours")
@login_required
def tournois_en_cours():
    return render_template('tournois_en_cours.html')


@app.get("/paris/tournoisEnCours/grandsChelems")
@login_required
def grands_chelems():
    return render_template('grands_chelems.html')


@app.get("/classement/joueur/<int:joueur_id>")
def fiche_joueur(joueur_id):
    joueur = get_joueur(joueur_id)
    if not joueur:
        print('no joueur')
        abort(404)
    chemin_fichier = os.path.join(app.root_path, joueur['fichier_html'])
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
    except FileNotFoundError:
        print('pas de fichier' )
        abort(404)
    return render_template('joueur.html', joueur=joueur, contenu=contenu)

if __name__ == '__name__':
    app.run(host='localhost', port=5000, debug=True)