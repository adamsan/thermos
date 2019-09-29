from datetime import datetime
# from thermos.thermos import db
from thermos import db


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    description = db.Column(db.String(300))

    def __repr__(self):
        return f"<Bookmark {self.description}: {self.url}>"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f"<User {self.username}>"


def create_db():
    print("Creating database...")
    db.create_all()
