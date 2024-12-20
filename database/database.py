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
               fichier_html TEXT NOT NULL,
               points INTEGER
               )''')
    
    joueurs = [
    (1, 'Jannik Sinner', 'static/joueurs/jannik_sinner.html', 11830),
    (2, 'Alexander Zverev', 'static/joueurs/alexander_zverev.html', 7915),
    (3, 'Carlos Alcaraz', 'static/joueurs/carlos_alcaraz.html', 7010),
    (4, 'Taylor Fritz', 'static/joueurs/taylor_fritz.html', 5100),
    (5, 'Daniil Medvedev', 'static/joueurs/daniil_medvedev.html', 5030),
    (6, 'Casper Ruud', 'static/joueurs/casper_ruud.html', 4255),
    (7, 'Novak Djokovic', 'static/joueurs/novak_djokovic.html', 3910),
    (8, 'Andrey Rublev', 'static/joueurs/andrey_rublev.html', 3760),
    (9, 'Alex de Minaur', 'static/joueurs/alex_de_minaur.html', 3745),
    (10, 'Grigor Dimitrov', 'static/joueurs/grigor_dimitrov.html', 3350),
    (11, 'Stefanos Tsitsipas', 'static/joueurs/stefanos_tsitsipas.html', 3165),
    (12, 'Tommy Paul', 'static/joueurs/tommy_paul.html', 3145),
    (13, 'Holger Rune', 'static/joueurs/holger_rune.html', 3025),
    (14, 'Karen Khachanov', 'static/joueurs/karen_khachanov.html', 2765),
    (15, 'Hubert Hurkacz', 'static/joueurs/hubert_hurkacz.html', 2685),
    (16, 'Frances Tiafoe', 'static/joueurs/frances_tiafoe.html', 2640),
    (17, 'Felix Auger-Aliassime', 'static/joueurs/felix_auger-aliassime.html', 2600),
    (18, 'Alexander Bublik', 'static/joueurs/alexander_bublik.html', 2585),
    (19, 'Lorenzo Musetti', 'static/joueurs/lorenzo_musetti.html', 2410),
    (20, 'Cameron Norrie', 'static/joueurs/cameron_norrie.html', 2355),
    (21, 'Sebastian Korda', 'static/joueurs/sebastian_korda.html', 2300),
    (22, 'Daniel Evans', 'static/joueurs/daniel_evans.html', 2250),
    (23, 'Denis Shapovalov', 'static/joueurs/denis_shapovalov.html', 2205),
    (24, 'Diego Schwartzman', 'static/joueurs/diego_schwartzman.html', 2150),
    (25, 'Roberto Bautista Agut', 'static/joueurs/roberto_bautista_agut.html', 2105),
    (26, 'Pablo Carreno Busta', 'static/joueurs/pablo_carreno_busta.html', 2050),
    (27, 'Gael Monfils', 'static/joueurs/gael_monfils.html', 2005),
    (28, 'John Isner', 'static/joueurs/john_isner.html', 1960),
    (29, 'Borna Coric', 'static/joueurs/borna_coric.html', 1920),
    (30, 'Nikoloz Basilashvili', 'static/joueurs/nikoloz_basilashvili.html', 1880),
    (31, 'Fabio Fognini', 'static/joueurs/fabio_fognini.html', 1840),
    (32, 'Reilly Opelka', 'static/joueurs/reilly_opelka.html', 1800),
    (33, 'Aslan Karatsev', 'static/joueurs/aslan_karatsev.html', 1760),
    (34, 'Dusan Lajovic', 'static/joueurs/dusan_lajovic.html', 1720),
    (35, 'Filip Krajinovic', 'static/joueurs/filip_krajinovic.html', 1680),
    (36, 'Albert Ramos-Vinolas', 'static/joueurs/albert_ramos-vinolas.html', 1640),
    (37, 'Ugo Humbert', 'static/joueurs/ugo_humbert.html', 1600),
    (38, 'Adrian Mannarino', 'static/joueurs/adrian_mannarino.html', 1560),
    (39, 'Jenson Brooksby', 'static/joueurs/jenson_brooksby.html', 1520),
    (40, 'Lloyd Harris', 'static/joueurs/lloyd_harris.html', 1480),
    (41, 'Marton Fucsovics', 'static/joueurs/marton_fucsovics.html', 1440),
    (42, 'Alexei Popyrin', 'static/joueurs/alexei_popyrin.html', 1400),
    (43, 'Emil Ruusuvuori', 'static/joueurs/emil_ruusuvuori.html', 1360),
    (44, 'Benoit Paire', 'static/joueurs/benoit_paire.html', 1320),
    (45, 'Richard Gasquet', 'static/joueurs/richard_gasquet.html', 1280),
    (46, 'Jo-Wilfried Tsonga', 'static/joueurs/jo-wilfried_tsonga.html', 1240),
    (47, 'Fernando Verdasco', 'static/joueurs/fernando_verdasco.html', 1200),
    (48, 'Sam Querrey', 'static/joueurs/sam_querrey.html', 1160),
    (49, 'Pablo Andujar', 'static/joueurs/pablo_andujar.html', 1120),
    (50, 'Jeremy Chardy', 'static/joueurs/jeremy_chardy.html', 1080),
    (51, 'Dominik Koepfer', 'static/joueurs/dominik_koepfer.html', 1040),
    (52, 'Jan-Lennard Struff', 'static/joueurs/jan-lennard_struff.html', 1000),
    (53, 'Yoshihito Nishioka', 'static/joueurs/yoshihito_nishioka.html', 960),
    (54, 'Mackenzie McDonald', 'static/joueurs/mackenzie_mcdonald.html', 920),
    (55, 'James Duckworth', 'static/joueurs/james_duckworth.html', 880),
]
    db.executemany('''INSERT OR REPLACE INTO joueurs (id, nom_complet, fichier_html, points) VALUES (?, ?, ?, ?)''', joueurs)


    db.execute('''CREATE TABLE IF NOT EXISTS questions (
               id INTEGER PRIMARY KEY,
               question TEXT NOT NULL,
               reponse TEXT NOT NULL
               )''')
    db.commit()
    
    questions = [
    (1, "Qui détient le record de titres à Wimbledon ?", "Roger Federer"),
    (2, "Qui détient le record de victoires à Roland-Garros ?", "Rafael Nadal"),
    (3, "Qui détient le record de semaines passées en tant que numéro 1 mondial ?", "Novak Djokovic"),
    (4, "Quelle joueuse a remporté le plus de titres en Grand Chelem dans l'ère Open ?", "Serena Williams"),
    (5, "Quel joueur britannique a remporté Wimbledon en 2013 et 2016 ?", "Andy Murray")
    ]
    db.executemany('''INSERT OR REPLACE INTO questions (id, question, reponse) VALUES (?, ?, ?)''', questions)
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

def get_questions():
    db = get_db()
    result = db.execute('SELECT * FROM questions').fetchall()
    db.close()
    return result