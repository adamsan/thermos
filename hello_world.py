#!/bin/python3

from flask import Flask

app = Flask(__name__)


#http://127.0.0.1:5000/index
@app.route('/index')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

# in python repl:
# import hello_world
# hello_world.app.url_map
# >Out[3]:
# Map([<Rule '/index' (HEAD, OPTIONS, GET) -> index>,
# <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>])
