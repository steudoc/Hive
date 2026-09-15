import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date

app = Flask(__name__)

# Configura la cartella di upload
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

# Crea la cartella se non esiste
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

posts = [{
        "id": 1,
        "username": "luigi",
        "data_pubblicazione": "2 giorni fa",
        "testo": "Ciao a tutti! 👋  "
        "Sono Luigi, il fratello minore di Mario! Oggi voglio condividere con voi una delle mie avventure più emozionanti. 🎮 "
        "Recentemente, ho esplorato una magione infestata piena di fantasmi e misteri. 🏰👻 Con il mio fidato Poltergust, ho catturato tutti i fantasmi e risolto enigmi complicati. Nonostante le sfide, sono riuscito a salvare la giornata e a riportare la pace nella magione. "
        "Essere un eroe non è facile, ma con coraggio e determinazione, tutto è possibile! 💪✨ "
        "E voi, avete mai affrontato una sfida che sembrava impossibile? Raccontatemi le vostre storie! 😊 ",
        "immagine_profilo": "/static/images/luigi.png",
        "immagine_post": "/static/images/img_luigi.png",
        "hashtags": ["avventura", "fantasmi", "coraggio", "determinazione"]
    }, {
        "id": 2,
        "username": "alberto",
        "data_pubblicazione": "4 giorni fa",
        "testo": "Recentemente, ho avuto l'opportunità di visitare un sito archeologico straordinario, ricco di storia e misteri. 🏺🔍 Camminando tra le antiche rovine, ho potuto sentire il peso del tempo e immaginare le vite delle persone che un tempo abitavano questi luoghi. Ogni pietra racconta una storia, e ogni scoperta ci avvicina un po' di più alla comprensione delle nostre origini. "
        "La passione per la conoscenza e la curiosità sono le chiavi che ci permettono di esplorare il passato e di costruire un futuro migliore. 🔑📚",
        "immagine_profilo": "/static/images/alberto.jpg",
        "immagine_post": "/static/images/img_alberto.JPG",
        "hashtags": ["ulisserai", "storia", "ilpiaceredellascoperta"]
    }, {
        "id": 3,
        "username": "juan",
        "data_pubblicazione": "4 giorni fa",
        "testo": "Grande vittoria oggi! 💪⚽️ Orgoglioso della squadra e del nostro impegno. Avanti così! 🔥",
        "immagine_profilo": "/static/images/juan.jpg",
        "immagine_post": "/static/images/img_juan.jpg",
        "hashtags": ["ForzaNapoli", "greatwin", "squadra", "anemaecore"]
    }, {
        "id": 4,
        "username": "steudoc",
        "data_pubblicazione": "5 giorni fa",
        "testo": "🚀 Benvenuti nel nostro social network! 🌐 Sono entusiasta di presentarvi questa nuova piattaforma che ho fondato con l'obiettivo di connettere persone, idee e passioni. 💡✨ Qui troverete uno spazio dove condividere esperienze, scoprire nuovi interessi e creare legami significativi. Unitevi a noi e diventate parte di questa straordinaria comunità! 🌟",
        "immagine_profilo": "/static/images/steudoc.JPG",
        "immagine_post": "/static/images/img_steudoc.jpeg",
        "hashtags": ["Founder", "Innovazione", "Connettiti", "Community"]
    }]

user_list = [
    {
        "username": "luigi",
        "immagine_profilo": "/static/images/luigi.png",
        "nome": "Luigi 🌟",
        "bio": "Avventuriero a tempo pieno, fratello di Mario e maestro di salti! 🏃‍♂️👾 Sempre pronto a salvare il Regno dei Funghi e a sconfiggere Bowser. 🎮🍄",
        "hashtags": ["SuperLuigi", "HeroInGreen"]
    }, {
        "username": "alberto",
        "immagine_profilo": "/static/images/alberto.jpg",
        "nome": "Alberto Angela 📚",
        "bio": "Divulgatore scientifico, esploratore e narratore di storie affascinanti. 🌍🧠 Portando la cultura e la storia nelle case di tutti.",
        "hashtags": ["curiosità", "scienza", "storia"]
    }, {
        "username": "juan",
        "immagine_profilo": "/static/images/juan.jpg",
        "nome": "Juan Jesus ⚽️",
        "bio": " Difensore centrale del Napoli, sempre pronto a proteggere la porta. 💪🔵 Passione per il calcio e determinazione in campo.",
        "hashtags": ["ForzaNapoli", "defender", "football"]
    }, {
        "username": "steudoc",
        "immagine_profilo": "/static/images/steudoc.JPG",
        "nome": "Stefano Tallone 🚀",
        "bio": "Visionario e innovatore, fondatore del nostro social network. 🌐💡 Appassionato di tecnologia e sempre alla ricerca di nuove idee per connettere le persone.",
        "hashtags": ["Founder", "Innovazione", "TechLover"]
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts, p_users=user_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post_selected = posts[post_id - 1]
    return render_template('post.html', p_post=post_selected)

@app.route('/user/<username>')
def user(username):
    user_posts = [post for post in posts if post['username'] == username]
    user_selected = next((user for user in user_list if user['username'] == username), None)
    return render_template('user.html', posts=user_posts, p_user=user_selected)

@app.route('/new_post', methods=['POST'])
def new_post():
    post = request.form.to_dict()

    if post['username'] not in [d['username'] for d in posts]:
            app.logger.error("Non esiste l'utente!")
            return redirect(url_for('home'))
    
    if post['testo'] == '':
            app.logger.error('Il post non può essere vuoto!')
            return redirect(url_for('home'))
    
    if post['data_pubblicazione'] == '':
            app.logger.error('Devi selezionare una data')
            return redirect(url_for('home'))
    
    if datetime.strptime(post['data_pubblicazione'], '%Y-%m-%d').date() < date.today():
            app.logger.error('Data errata')
            return redirect(url_for('home'))
    
    post_image = request.files['immagine_post']
    if post_image:
        post_image.save('static/' + post_image.filename)
        post['immagine_post'] = post_image.filename
    else:
        post['immagine_post'] = 'static/images/no_image.png'

    # Cerca l'immagine profilo nella lista degli utenti
    user = next((u for u in user_list if u['username'] == post['username']), None)
    if user:
        post['immagine_profilo'] = user['immagine_profilo']
    else:
        app.logger.error("Immagine profilo non trovata per l'utente!")
        return redirect(url_for('home'))

    post['id'] = posts[-1]['id'] + 1
    posts.append(post)

    # Debug: stampa il contenuto del dizionario posts
    print("Dizionario dei post aggiornato:", posts)

    return redirect(url_for("home"))