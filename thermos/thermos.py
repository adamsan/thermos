#!/bin/python3
import os
from typing import List
from flask import Flask, render_template, url_for, request, redirect
from flask import flash, session
from flask_sqlalchemy import SQLAlchemy
import logging
import datetime
import models
from sqlalchemy.exc import OperationalError

from forms import BookmarkForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.secret_key = 'this_is_super_secret123'  # import os; os.urandom(24)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.logger.setLevel(logging.DEBUG)
db = SQLAlchemy(app)


def store_bookmark(url, description):
    try:
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
    except OperationalError:
        models.create_db()


def new_bookmarks(num: int) -> List[dict]:
    try:
        return db.session().query(models.Bookmark).all()
    except OperationalError:
        models.create_db()
    finally:
        return db.session().query(models.Bookmark).all()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url, description = form.url.data, form.description.data
        store_bookmark(url, description)
        flash(f"stored url: {url}")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
