import sqlite3

def new_comment(comment):
    sql = "INSERT INTO commenti (data_pubblicazione, testo, id_post, id_utente, valutazione, immagine_commento) VALUES (?, ?, ?, ?, ?, ?)"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(sql, (comment['data_pubblicazione'], comment['testo'], comment['id_post'], comment['id_utente'], comment['valutazione'], comment['immagine_commento']))
    conn.commit()
    conn.close()

def get_commenti_by_post(post_id):
    sql = """
    SELECT c.*, u.username, u.immagine_profilo
    FROM commenti c
    JOIN utenti u ON c.id_utente = u.id
    WHERE c.id_post = ?
    """
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    cursor = conn.cursor()
    cursor.execute(sql, (post_id,))
    commenti = cursor.fetchall()
    conn.close()
    
    return commenti