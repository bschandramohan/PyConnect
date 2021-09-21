from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dbFlask = Flask(__name__)
dbFlask.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///User.db"
db = SQLAlchemy(dbFlask)


class User(db.Model):
    username = db.Column("username", db.String(100), primary_key=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        # print("init called")
        # db.create_all()
        self.username = username
        self.password = password


def __init__():
    db.create_all()


def store_user(username, password) -> bool:
    result = User.query.get(username)
    if result is None:
        print(username, password)
        db.session.add(User(username, password))
        db.session.commit()
        return True
    else:
        print("user already exists")
        return False


def is_user_login_correct(username, password) -> bool:
    result = User.query.get(username)
    print(result)
    if result is None:
        print("user doesn't exists")
    else:
        if password == result.password:
            print("Logged In")
            return True
        else:
            print("Wrong password")

    return False
