from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
# 3 forward slash - relative path
# 4 forward slash - absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
    os.path.join(basedir, 'Data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password


class Contact(db.Model):
    __tablename__ = 'contact'
    name = db.Column(db.String(120), nullable=False, unique=False)
    email = db.Column(db.String(120), nullable=False, unique=False)
    message = db.Column(db.String(1200), primary_key=True, nullable=False)

    def __init__(self, name=None, email=None, message=None):
        self.name = name
        self.email = email
        self.message = message


class Notes(db.Model):
    __tablename__ = 'notes'
    title = db.Column(db.String(1200), nullable=False, primary_key=True)
    content = db.Column(db.String(1200), nullable=False, unique=False)

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

