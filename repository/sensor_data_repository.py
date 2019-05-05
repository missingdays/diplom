

from mysql.connector import (connection)
import mysql

from .repository import Repository
from .sensor_repository import SensorRepository
from dataclasses import dataclass

class SensorDataRepository(Repository):
    table = 'sensor_data'

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
                    `process_id` int(11) NOT NULL,
                    `sensor_id` int(11) NOT NULL,
                    `value` int(11),
                    PRIMARY KEY (`id`),
                    FOREIGN KEY (sensor_id) REFERENCES {}(id)
                )
                """.format(self.table, SensorRepository.table)
            )
        except mysql.connector.Error as err:
            print(err.msg)

        cursor.close()

    def add_entity(self, sensor_data):
        cursor = self.cnx.cursor()

        query = """INSERT INTO {}
                (sensor_id, process_id, value)
                VALUES (%s, %s, %s)
            """.format(self.table)
        
        cursor.execute(
            query,
            [sensor_data.sensor_id, sensor_data.process_id, sensor_data.value]
        )

        self.cnx.commit()
        ret_id = cursor.lastrowid

        cursor.close()

        return ret_id

    def get_entity(self, id):
        cursor = self.cnx.cursor()

        cursor.execute(
            """SELECT id, sensor_id, process_id, value FROM {}
               WHERE id=%s
            """.format(self.table),

            [id]
        )

        sensor_datas = cursor.fetchall()

        if not sensor_datas:
            raise Exception("Can't find id {}".format(id))

        sensor_data = sensor_datas[0]

        cursor.close()

        return SensorData(id=sensor_data[0], sensor_id=sensor_data[1], process_id=sensor_data[2], value=sensor_data[3])

@dataclass
class SensorData:
    id: int
    sensor_id: int
    process_id: int
    value: int
