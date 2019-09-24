#!/bin/python3

from flask import Flask, render_template, url_for, request, redirect
import logging
import datetime

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

bookmarks = []


def store_bookmark(url):
    bookmarks.append({
        'url': url,
        'user': 'adamsan',
        'date': datetime.datetime.utcnow()
    })


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
    return render_template('index.html', data=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug(f"stored url: {url}")
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
