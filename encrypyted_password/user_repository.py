from init import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import *


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///User.db"
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
        db.session.add(User(username, password))
        db.session.commit()
        return True
    else:
        return False


def is_user_login_correct(username, password):
    result = User.query.get(username)
    if result is not None:
        if result.password == password:
            return True

    return False
