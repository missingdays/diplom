
from .config import config
import mysql

cache = {}

def get_connection(db):
    return cache.setdefault(db, mysql.connector.connect(
            **config,
            database=db
        )
    )
