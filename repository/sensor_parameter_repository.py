
from mysql.connector import (connection)
import mysql

from .repository import Repository
from .sensor_repository import SensorRepository
from dataclasses import dataclass

class SensorParameterRepository(Repository):
    table = 'sensor_parameters'

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
                    `sensor_id` int(11) NOT NULL,
                    `name` varchar(16) NOT NULL,
                    `value` int(11),
                    PRIMARY KEY (`id`),
                    FOREIGN KEY (sensor_id) REFERENCES {}(id)
                )
                """.format(self.table, SensorRepository.table)
            )
        except mysql.connector.Error as err:
            print(err.msg)

        cursor.close()

    def add_entity(self, sensor_parameter):
        cursor = self.cnx.cursor()

        query = """INSERT INTO {}
                (sensor_id, name, value)
                VALUES (%s, %s, %s)
            """.format(self.table)
        
        cursor.execute(
            query,
            [sensor_parameter.sensor_id, sensor_parameter.name, sensor_parameter.value]
        )

        self.cnx.commit()
        ret_id = cursor.lastrowid

        cursor.close()

        return ret_id

    def get_entity(self, id):
        cursor = self.cnx.cursor()

        cursor.execute(
            """SELECT id, sensor_id, name, value FROM {}
               WHERE id=%s
            """.format(self.table),

            [id]
        )

        sensor_parameters = cursor.fetchall()

        if not sensor_parameters:
            raise Exception("Can't find id {}".format(id))

        sensor_parameter = sensor_parameters[0]

        cursor.close()

        return SensorParameter(id=sensor_parameter[0], sensor_id=sensor_parameter[1], name=sensor_parameter[2], value=sensor_parameter[3])

@dataclass
class SensorParameter:
    id: int
    sensor_id: int
    name: str
    value: int
