from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tags.db'
db = SQLAlchemy(app)


class Tags(db.Model):
    id = db.Column('tag_id', db.Integer, primary_key=True)
    tag = db.Column(db.String(100))


def __init__(self, tag_value):
    self.tag = tag_value
    db.create_all()


@app.route("/")
def get_all():
    result = Tags.query.all()
    if result is None:
        return "No Tags available Yet"
    else:
        print(result)
        tags_list = [record.tag for record in result]
        return "\t - \n".join(tags_list)


@app.route("/<id>")
def get(tag_id):
    result = Tags.query.get(tag_id)
    print(result)
    return result


@app.route("/tag/<tag_value>", methods=["GET"])
def add(tag_value):
    existing_tag = Tags.query.filter_by(tag=tag_value).all()
    if existing_tag is None or len(existing_tag) == 0:
        db.session.add(Tags(tag=tag_value))
        db.session.commit()
        return "SUCCESS"
    else:
        return "DUPLICATE"


if __name__ == "__main__":
    app.run(debug=True)
