
from mysql.connector import (connection)
import mysql

from .repository import Repository
from dataclasses import dataclass

class ResultRepository(Repository):
    table = 'result'

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
                    `result` int(11) NOT NULL,
                    PRIMARY KEY (`id`))
                """.format(self.table)
            )
        except mysql.connector.Error as err:
            print(err.msg)

        cursor.close()

    def add_entity(self, result):
        cursor = self.cnx.cursor()

        query = """INSERT INTO {}
                (process_id, result)
                VALUES (%s, %s)
            """.format(self.table)
        
        cursor.execute(
            query,
            [result.process_id, result.result]
        )

        self.cnx.commit()
        ret_id = cursor.lastrowid

        cursor.close()

        return ret_id

    def get_entity(self, id):
        cursor = self.cnx.cursor()

        cursor.execute(
            """SELECT id, process_id, result FROM {}
               WHERE id=%s
            """.format(self.table),

            [id]
        )

        results = cursor.fetchall()

        if not results:
            raise Exception("Can't find id {}".format(id))

        result = Result(id=results[0][0], process_id=results[0][1], result=results[0][2])

        cursor.close()

        return result

    def get_all(self):
        cursor = self.cnx.cursor()

        cursor.execute(
            """SELECT id, process_id, result FROM {}
            """.format(self.table),
            []
        )

        results = cursor.fetchall()

        if not results:
            return []

        result = map(lambda x: Result(id=x[0], process_id=x[1], result=x[2]), results)

        cursor.close()

        return result

@dataclass
class Result:
    id: int
    process_id: int
    result: int
