DATABASES = {
    'postgresql': 'postgresql://{}:{}@{}/{}',
    'mysql': 'mysql+pymysql://{}:{}@{}/{}',
    'oracle': 'oracle://{}:{}@{}/{}',
    'mssql': 'mssql+pyodbc://{}:{}@{}/{}',
    'sqlite': 'sqlite:///{}',
    'firebird': 'firebird://{}:{}@{}/{}',
}

from sqlalchemy import create_engine
import psycopg2
import pymysql

DATABASES = {
    'postgresql': 'postgresql://{}:{}@{}/{}',
    'mysql': 'mysql+pymysql://{}:{}@{}/{}',
}

HOST = 'aws.connect.psdb.cloud'
USERNAME = '[xxx]'
PASSWORD = '[xxx]'
DATABASE = 'ida4health'

def try_connect():
    for db, url in DATABASES.items():
        try:
            engine = create_engine(url.format(USERNAME, PASSWORD, HOST, DATABASE))
            connection = engine.connect()
            print(f'Successfully connected with {db}!')
            return db
        except Exception as e:
            print(f'Failed to connect with {db}: {e}')
    return None

try_connect()
