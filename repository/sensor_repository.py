from mysql.connector import (connection)
import mysql

from .repository import Repository
from dataclasses import dataclass

class SensorRepository(Repository):
    table = 'sensors'

    def __init__(self):
        super().__init__()

        self.create_table()

    def create_table(self):
        cursor = self.cnx.cursor()

        print("CREATING TABLE {}".format(self.table))

        try:
            cursor.execute(
                """CREATE TABLE {}(
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `name` varchar(16) NOT NULL,
                    PRIMARY KEY (`id`))
                """.format(self.table)
            )
        except mysql.connector.Error as err:
            print(err.msg)

        cursor.close()

    def add_entity(self, sensor):
        cursor = self.cnx.cursor()

        query = """INSERT INTO {}
                (name)
                VALUES (%s)
            """.format(self.table)
        
        cursor.execute(
            query,
            [sensor.name]
        )

        self.cnx.commit()
        ret_id = cursor.lastrowid

        cursor.close()

        return ret_id

    def get_entity(self, id):
        cursor = self.cnx.cursor()

        cursor.execute(
            """SELECT id, name FROM {}
               WHERE id=%s
            """.format(self.table),

            [id]
        )

        sensors = cursor.fetchall()

        if not sensors:
            raise Exception("Can't find id {}".format(id))

        sensor = Sensor(id=sensors[0][0], name=sensors[0][1])

        cursor.close()

        return sensor

@dataclass
class Sensor:
    id: int
    name: str
