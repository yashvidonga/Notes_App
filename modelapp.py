from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 3 forward slash - relative path
# 4 forward slash - absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename_ = 'users'
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

class Contact(db.Model):
    __tablename_ = 'contact'
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(1200), primary_key=True, nullable=False)

    def __init__(self, name=None, email=None, message=None):
        self.name = name
        self.email = email
        self.message = message