from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Flask instance
app = Flask(__name__)
#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ekrypto.db'
#Secret key
app.config['SECRET_KEY'] = '12345'
#Initialize database
db = SQLAlchemy(app)

#Create model for database
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    profile_pic = db.Column(db.String, nullable=False)

    #Return a JSON
    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self, 'profile_pic': self.profile_pic}


#instanciando/criando banco de dados
with app.app_context():
    db.create_all()


