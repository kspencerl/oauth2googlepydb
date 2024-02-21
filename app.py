#pip install -r requirements.txt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#instanciar Flask
app = Flask(__name__)
#adicionar database sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ekrypto.db' #nome para o database
#configurar password
app.config['SECRET_KEY'] = '12345' #senha para o database
#inicializar banco de dados
db = SQLAlchemy(app)

#criar modelo para o banco de dados
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    profile_pic = db.Column(db.String, nullable=False)

    #retornar JSON
    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self, 'profile_pic': self.profile_pic}


#instanciar/criar banco de dados
with app.app_context():
    db.create_all()


