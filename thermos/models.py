from datetime import datetime
# from thermos.thermos import db
from sqlalchemy import desc

from thermos import db


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Bookmark {self.description}: {self.url}>"

    @staticmethod
    def newest(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    bookmarks = db.relationship('Bookmark', backref='user', lazy='dynamic')

    def __repr__(self):
        return f"<User {self.username}>"


def create_db():
    print("Creating database...")
    db.create_all()
    db.session.add(User(username='adam', email='adam@adam.net'))
    db.session.add(User(username='peter', email='peter@adam.net'))
    db.session.commit()
# ipython
# cd thermos
# E:\flask_learn\flask_project\thermos
# import thermos
# import models
# a = models.User.query.get(1)
# for url,descr in [('http://www.prog.hu','HUN programmer site'),('http://www.index.hu','news site')]:
#      thermos.db.session.add(models.Bookmark(user=a, url=url, description=descr))
# thermos.db.session.commit()
# a.bookmarks.all()
