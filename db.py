import databases
import sqlalchemy
import os

DATABASE = 'mysql'
USER = os.environ.get('DB_USERNAME')
PASSWORD = os.environ.get('DB_PASSWORD')
HOST = os.environ.get('DB_HOST')
PORT = '3306'
DB_NAME = os.environ.get('DB_DATABASE')

DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(
    DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

# databases
database = databases.Database(DATABASE_URL, min_size=5, max_size=20)

ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)

metadata = sqlalchemy.MetaData()
