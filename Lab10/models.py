from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, email, password, immagine_profilo):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.immagine_profilo = immagine_profilo