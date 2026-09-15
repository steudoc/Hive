from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date, timedelta

import os, posts_dao, utenti_dao, commenti_dao

app = Flask(__name__)

# Configura la cartella di upload
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

# Crea la cartella se non esiste
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    post_list = posts_dao.get_posts()
    user_list = utenti_dao.get_utenti()
    return render_template('home.html', posts=post_list, p_users=user_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/oggi')
def post_oggi():
    today = date.today()
    post_list = posts_dao.get_posts()
    user_list = utenti_dao.get_utenti()
    posts_today = [post for post in post_list if datetime.strptime(post['data_pubblicazione'], "%Y-%m-%d").date() == today]
    return render_template('home.html', posts=posts_today, p_users=user_list, active_filter='oggi')

@app.route('/post/ultimi_7_giorni')
def post_ultimi_7_giorni():
    post_list = posts_dao.get_posts()
    user_list = utenti_dao.get_utenti()
    today = date.today()
    last_7_days = today - timedelta(days=7)
    posts_last_7_days = [post for post in post_list if datetime.strptime(post['data_pubblicazione'], "%Y-%m-%d").date() >= last_7_days]
    return render_template('home.html', posts=posts_last_7_days, p_users=user_list, active_filter='ultimi_7_giorni')

@app.route('/post/ultimi_30_giorni')
def post_ultimi_30_giorni():
    post_list = posts_dao.get_posts()
    user_list = utenti_dao.get_utenti()
    today = date.today()
    last_30_days = today - timedelta(days=30)
    posts_last_30_days = [post for post in post_list if datetime.strptime(post['data_pubblicazione'], "%Y-%m-%d").date() >= last_30_days]
    return render_template('home.html', posts=posts_last_30_days, p_users=user_list, active_filter='ultimi_30_giorni')

@app.route('/post/<int:post_id>')
def post(post_id):
    post_selected = posts_dao.get_post_by_id(post_id)
    commenti_list = commenti_dao.get_commenti_by_post(post_id)
    user_list = utenti_dao.get_utenti()
    return render_template('post.html', p_post=post_selected, p_users=user_list, p_commenti=commenti_list)

@app.route('/user/<username>')
def user(username):
    user_selected = utenti_dao.get_utente(username)
    posts_list = posts_dao.get_posts_by_user(user_selected['id'])
    return render_template('user.html', posts=posts_list, p_user=user_selected)

@app.route('/new_comment/<int:post_id>', methods=['POST'])
def new_comment(post_id):
    comment = request.form.to_dict()

    if comment['data_pubblicazione'] == '':
            app.logger.error('Devi selezionare una data')
            return redirect(url_for('post', post_id=post_id))
    if datetime.strptime(comment['data_pubblicazione'], "%Y-%m-%d").date() > date.today():
            app.logger.error('Data errata')
            return redirect(url_for('post', post_id=post_id))
    
    if comment['testo'] == '':
            app.logger.error('Il commento non può essere vuoto!')
            return redirect(url_for('post', post_id=post_id))
    
    comment['id_utente'] = int(comment['id_utente'])
    comment['id_post'] = post_id
    comment['valutazione'] = int(comment.get('valutazione', 0))

    # Salva l'immagine del commento se presente
    comment_image = request.files['immagine_commento']
    if comment_image:
        comment_image.save('static/uploads/' + comment_image.filename)
        comment['immagine_commento'] = f"/static/uploads/{comment_image.filename}"
    else:
        comment['immagine_commento'] = '/static/images/no_image.png'
    
    commenti_dao.new_comment(comment)
    
    return redirect(url_for('post', post_id=post_id))

@app.route('/new_post', methods=['POST'])
def new_post():
    post = request.form.to_dict()

    if post['data_pubblicazione'] == '':
            app.logger.error('Devi selezionare una data')
            return redirect(url_for('home'))
    if datetime.strptime(post['data_pubblicazione'], "%Y-%m-%d").date() > date.today():
            app.logger.error('Data errata')
            return redirect(url_for('home'))
    
    if post['testo'] == '':
            app.logger.error('Il post non può essere vuoto!')
            return redirect(url_for('home'))
    
    post_image = request.files['immagine_post']
    if post_image:
        post_image.save('static/uploads/' + post_image.filename)
        post['immagine_post'] = f"/static/uploads/{post_image.filename}"
    else:
        post['immagine_post'] = '/static/images/no_image.png'

    post['id_utente'] = int(post['id_utente'])

    # Processa gli hashtag
    #hashtags = post['hashtags']
    #post['hashtags'] = hashtags.split(' ') if hashtags else []

    # Debug: stampa il contenuto del dizionario posts
    print("Dizionario dei post aggiornato:", post)

    posts_dao.new_post(post)

    return redirect(url_for("home"))

@app.template_filter('format_date')
def format_date(date):
     date = datetime.strptime(date, "%Y-%m-%d").date()
     today = datetime.today().date()
     delta = today - date

     if delta.days == 0:
          return "Oggi"
     elif delta.days == 1:
          return "Ieri"
     elif delta.days < 7:
          return f"{delta.days} giorni fa"
     elif delta.days < 30:
          weeks = delta.days // 7
          return f"{weeks} settiman{'e' if weeks > 1 else 'a'} fa"
     else:
          return date.strftime("%d/%m/%Y")