#!/bin/python3
import click
import models
import thermos


@click.group()
def manage():
    pass


@manage.command()
def initdb():
    models.create_db()


@manage.command()
def dropdb():
    thermos.db.drop_all()


@manage.command()
def runserver():
    thermos.app.run(debug=True)


if __name__ == '__main__':
    manage()
