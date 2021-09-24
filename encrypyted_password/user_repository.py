from init import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import *


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///User.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column("username", db.String(100), primary_key=True)
    password = db.Column("password", db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


def init():
    db.create_all()


def store(username, password):
    result = User.query.get(username)
    if result is None:
        # Hash the password. Format stored will be :
        # password
        # pbkdf2:sha256:260000$a3VM9h8DnK6mM0kS$90248571d69d79d591d798a6cbe88309bd1d66b0333979694b1a0d6e3ee15639
        hash_of_password = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=16)
        db.session.add(User(username, hash_of_password))
        db.session.commit()
        return True
    else:
        return False


def is_user_login_correct(username, password):
    result = User.query.get(username)
    if result is not None:
        if check_password_hash(pwhash=result.password, password=password):
            return True

    return False
