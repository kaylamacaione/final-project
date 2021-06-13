import click
from flask.cli import with_appcontext
from .app import db, Destinations

@click.command(with_appcontext=False, name='create_tables')
def create_tables():
  # db.drop_all()
  db.create_all()
