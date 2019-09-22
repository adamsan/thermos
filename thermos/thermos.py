#!/bin/python3

from flask import Flask, render_template, url_for

app = Flask(__name__)

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


@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run()
