# FLASK CONFIGURATION FILE
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/dest_airports.sqlite'

class TestingConfig(Config):
    TESTING = True

from flask import Flask
from sqlalchemy import create_engine, select
import psycopg2
from models import Base


conn = psycopg2.connect("dbname=DB_NAME user")

engine_lite = create_engine()
engine_cloud = create_engine('postgresql+psycopg2://judwspdyelwnak:''@/postgresql-aerodynamic-26022?host:=ec2-34-233-114-40.compute-1.amazonaws.com/cloudsql/INSTANCE')

with engine_lite.connect() as conn_lite:
with engine_cloud.connect() as conn_cloud:
    for table in Base.metadata.sorted_tables:
        data = [dict(row) for row in conn_lite.execute(select(table.c))]
        conn_cloud.execute(table.insert().values(data))

app = Flask(__name__)
app.config.update(
		DEVELOPMENT=True,
		TOKEN="ajisdj2j19jdjaj9sd",
		SECRET_KEY="a9a9**d7s9asS*D6ˆDˆ678SD("
)
if __name__ == "__main__":
		app.run()