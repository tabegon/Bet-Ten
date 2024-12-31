import hashlib
import os
import sqlite3
from flask import Flask, abort, flash, redirect, render_template, request, session, url_for
from random import randint
from database.database import create_database, create_user, get_joueur, get_joueurs, get_question, get_questions, get_user, get_user_by_id, get_users, set_points
from decorator.auth import login_required
from helpers import check_password, encode_password



    
create_database()
app = Flask(__name__)

app.secret_key = 'super secret key'

@app.route("/")
def index():
    joueurs = get_joueurs()
    questions = get_questions()
    nombre = randint(1, 5)
    question = get_question(nombre)
    return render_template("/accueil.html", joueurs=joueurs, question=question['question'])



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

@app.get("/quiz")
@login_required
def quiz():
    questions = get_questions()
    return render_template('quiz.html', questions=questions)

@app.post('/quiz/validation')
@login_required
def validation_quiz():
    questions = get_questions()
    points_totaux = 0
    reponses_utilisateur = {}
    for question in questions:
        reponse_utilisateur = request.form.get('reponse-'+str(question['id']))
        if not reponse_utilisateur:
            pass
        if question['reponse'].lower() == reponse_utilisateur.lower():
            points_totaux += 10
            reponses_utilisateur[question['id']] = True
        else:
            reponses_utilisateur[question['id']] = False
    user_id = session['user_id']
    user = get_user_by_id(user_id)
    set_points(user_id, user['points']+points_totaux)
    session['user_points'] = user['points']+points_totaux
    return render_template('reponses_quiz.html', points=points_totaux, questions=questions, reponses_utilisateur=reponses_utilisateur) #Vous avez eu x points


@app.get("/paris")
@login_required
def paris():
    return render_template('paris.html')

@app.get("/paris/vosParis")
@login_required
def vos_paris():
    return render_template('vos_paris.html')

@app.get("/paris/tournoisEnCours")
@login_required
def tournois_en_cours():
    return render_template('tournois_en_cours.html')

@app.get("/paris/tournoisEnCours/atp1000")
@login_required
def atp_1000():
    return render_template('atp_1000.html')

@app.get("/paris/tournoisEnCours/atp500")
@login_required
def atp_500():
    return render_template('atp_500.html')

@app.get("/paris/tournoisEnCours/grandsChelems")
@login_required
def grands_chelems():
    return render_template('grands_chelems.html')

@app.get("/paris/tournoisEnCours/grandsChelems/match1")
@login_required
def match():
    return render_template('paris_match.html')

@app.post('/paris/tournoisEnCours/grandsChelems/match1/validation')
@login_required
def validation_pari():
    gagner_points = None
    soustraire_points = request.form.get('quantity_to_bet')
    chance_de_gagner = randint(1, 3)
    if chance_de_gagner == 2:
        gagner_points = int(soustraire_points)*2
    user_id = session['user_id']
    user = get_user_by_id(user_id)
    if session['user_points']>int(soustraire_points):
        if not gagner_points:
            points_necessaire = True
            set_points(user_id, user['points'] - int(soustraire_points))
            session['user_points'] = user['points'] - int(soustraire_points)
        else:
            points_necessaire = True
            set_points(user_id, user['points'] + gagner_points)
            session['user_points'] = user['points'] + gagner_points
            return render_template('reponse_pari.html', points=soustraire_points, points_necessaire=points_necessaire, issue=True)
    else:
        points_necessaire = False
    return render_template('reponse_pari.html', points=soustraire_points, points_necessaire=points_necessaire, issue=False)




@app.get("/classement")
def classement():
    joueurs = get_joueurs()
    return render_template('classement.html', joueurs=joueurs)

@app.get("/classement/joueur/<int:joueur_id>")
def fiche_joueur(joueur_id):
    joueur = get_joueur(joueur_id)
    if not joueur:
        abort(404)
    chemin_fichier = os.path.join(app.root_path, joueur['fichier_html'])
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
    except FileNotFoundError:
        abort(404)
    return render_template('joueur.html', joueur=joueur, contenu=contenu)

@app.get("/clssmntParieur")
@login_required
def classement_parieur():
    users = get_users()
    users_sorted = sorted(users, key=lambda x: x['points'], reverse=True)
    return render_template('classement_parieur.html', users=users_sorted)

if __name__ == '__name__':
    app.run(host='localhost', port=5000, debug=True)