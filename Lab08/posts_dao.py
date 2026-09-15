import sqlite3

def new_post(post):
        
        sql = "INSERT INTO posts (data_pubblicazione, testo, immagine_post, id_utente, hashtags) VALUES (?, ?, ?, ?, ?)"
    
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql, (post['data_pubblicazione'], post['testo'], post['immagine_post'], post['id_utente'], post['hashtags']))
        conn.commit()
        conn.close()

def get_posts():
    sql = """
    SELECT p.*, u.username, u.immagine_profilo
    FROM posts p
    JOIN utenti u ON p.id_utente = u.id
    """
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    cursor = conn.cursor()
    cursor.execute(sql)
    posts_with_users = cursor.fetchall()
    conn.close()
    
    return posts_with_users

def get_posts_by_user(user_id):
    sql = """
    SELECT p.*, u.username, u.immagine_profilo
    FROM posts p
    JOIN utenti u ON p.id_utente = u.id
    WHERE p.id_utente = ?
    """
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql, (user_id,))
    posts = cursor.fetchall()
    conn.close()
    
    return posts

def get_post_by_id(post_id):
    sql = """
    SELECT p.*, u.username, u.immagine_profilo
    FROM posts p
    JOIN utenti u ON p.id_utente = u.id
    WHERE p.id = ?
    """
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql, (post_id,))
    post = cursor.fetchone()
    conn.close()
    
    return post