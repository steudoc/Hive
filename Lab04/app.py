from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [{
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
        "username": "alberto",
        "data_pubblicazione": "4 giorni fa",
        "testo": "Recentemente, ho avuto l'opportunità di visitare un sito archeologico straordinario, ricco di storia e misteri. 🏺🔍 Camminando tra le antiche rovine, ho potuto sentire il peso del tempo e immaginare le vite delle persone che un tempo abitavano questi luoghi. Ogni pietra racconta una storia, e ogni scoperta ci avvicina un po' di più alla comprensione delle nostre origini. "
        "La passione per la conoscenza e la curiosità sono le chiavi che ci permettono di esplorare il passato e di costruire un futuro migliore. 🔑📚",
        "immagine_profilo": "/static/images/alberto.jpg",
        "immagine_post": "/static/images/img_alberto.JPG",
        "hashtags": ["ulisserai", "storia", "ilpiaceredellascoperta"]
    }, {
        "username": "juan",
        "data_pubblicazione": "4 giorni fa",
        "testo": "Grande vittoria oggi! 💪⚽️ Orgoglioso della squadra e del nostro impegno. Avanti così! 🔥",
        "immagine_profilo": "/static/images/juan.jpg",
        "immagine_post": "/static/images/img_juan.jpg",
        "hashtags": ["forzanapoli", "greatwin", "squadra", "anemaecore"]
    }]
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')