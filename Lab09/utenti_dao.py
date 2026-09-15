import sqlite3

def nuovo_utente(username, password, immagine_profilo, nome, bio, hashtags):
    
    sql = "INSERT INTO utenti (username, password, immagine_profilo, nome, bio, hashtags) VALUES (?, ?, ?, ?, ?, ?)"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(sql, (username, password, immagine_profilo, nome, bio, hashtags))
    conn.commit()
    conn.close()

def get_utenti():
    sql = "SELECT * FROM utenti WHERE id != 1"

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    cursor = conn.cursor()
    cursor.execute(sql)
    utenti = cursor.fetchall()
    conn.close()

    return utenti

def get_utente(username):
    sql = "SELECT * FROM utenti WHERE username = ?"

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    cursor = conn.cursor()
    cursor.execute(sql, (username,))
    utente = cursor.fetchone()
    conn.close()

    return utente

def get_utente_by_id(id_utente):
    sql = "SELECT * FROM utenti WHERE id = ?"

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql, (id_utente,))
    utente = cursor.fetchone()
    conn.close()

    return utente

def get_username_by_id(id_utente):
    sql = "SELECT username FROM utenti WHERE id = ?"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(sql, (id_utente,))
    username = cursor.fetchone()
    conn.close()

    return username[0] if username else None

def get_imm_by_id(id_utente):
    sql = "SELECT immagine_profilo FROM utenti WHERE id = ?"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(sql, (id_utente,))
    immagine_profilo = cursor.fetchone()
    conn.close()

    return immagine_profilo[0] if immagine_profilo else None

def get_user_by_email(email):
    sql = "SELECT * FROM utenti WHERE email = ?"

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    cursor = conn.cursor()
    cursor.execute(sql, (email,))
    utente = cursor.fetchone()
    conn.close()

    return utente

def new_user(user):
    sql = "INSERT INTO utenti (username, email, password, immagine_profilo, nome, bio, hashtags) VALUES (?, ?, ?, ?, ?, ?, ?)"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(sql, (user['username'], user['email'], user['password'], user['immagine_profilo'], user['nome'], user['bio'], user['hashtags']))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    sql = "SELECT * FROM utenti WHERE username = ?"

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    cursor = conn.cursor()
    cursor.execute(sql, (username,))
    utente = cursor.fetchone()
    conn.close()

    return utente
