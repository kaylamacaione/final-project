import os
import psycopg2
import urllib.parse as urlparse

# Copy sqlite db to Heroku postgres db
url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

conn = psycopg2.connect("dbname=postgresql-closed-50309 user=lzxksarpgkpyth password=47e0e4cac1240da05722d01fb4b1c8ac091d5d94d25f6716c68c4df448a618a9")
cur = conn.cursor()
with open('sqlite:///data/dest_airports.sqlite', 'r') as f:
    # Skip the header row
    next(f)
    cur.copy_from(f, 'dest_airports', sep=',')
conn.commit()
