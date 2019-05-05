import mysql.connector
from .config import config
from .connection import get_connection

class Repository:
    def __init__(self):
        self.database = 'diplom'

        self.create_db()
        self.cnx = get_connection(self.database)

    def create_db(self):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        print("CREATING DB {}".format(self.database))
        
        try:
            cursor.execute(
                    "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.database))
        except mysql.connector.Error as err:
            print(err.msg)

        cursor.close()

    def drop(self):
        cursor = self.cnx.cursor()

        print("DROPPING {}".format(self.table))

        try:
            cursor.execute("DROP TABLE {}".format(self.table))
        except Exception as e:
            print(e.msg)

        self.cnx.commit()

        cursor.close()
