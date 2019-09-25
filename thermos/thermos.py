#!/bin/python3
import os
from typing import List
from flask import Flask, render_template, url_for, request, redirect
from flask import flash, session
import logging
import datetime

app = Flask(__name__)
#app.secret_key = 'this_is_super_secret123'  # import os; os.urandom(24)
app.config['SECRET_KEY'] = os.urandom(24)
app.logger.setLevel(logging.DEBUG)

bookmarks = []


def store_bookmark(url):
    bookmarks.append({
        'url': url,
        'user': 'adamsan',
        'date': datetime.datetime.utcnow()
    })


def new_bookmarks(num: int) -> List[dict]:
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return f"{self.firstname} {self.lastname}"


@app.route('/')
@app.route('/index')
def index():
    data = User('Albert', 'Einstein')
    return render_template('index.html', data=data, new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug(f"stored url: {url}")
        flash(f"stored url: {url}")
        return redirect(url_for('index'))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
