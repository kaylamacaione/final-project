import click
from flask.cli import with_appcontext
from .app import db, Destinations

@click.command(name='create_tables')
@with_appcontext
def create_tables():
  # db.drop_all()
  db.create_all()
