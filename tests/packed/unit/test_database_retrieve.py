import mysql.connector
import unittest
from tests.packed.test_database import TestDatabase


def retrieve_database(connection: mysql.connector.MySQLConnection):
    """Gets database table values"""

    cursor = connection.cursor()

    query = 'SELECT * FROM test_table'

    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except mysql.connector.errors.ProgrammingError as error:
        result = ("Error retrieving data from MySQL database:", str(error))
    return result


class TestRetrieveDatabase(TestDatabase):
    def test_retrieve_database(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO test_table (id, name, age) VALUES (1, 'John', 25)"
            )
        cursor.execute(
            "INSERT INTO test_table (id, name, age) VALUES (2, 'Jane', 30)"
            )
        self.connection.commit()

        result = retrieve_database(self.connection)

        expected_result = [(1, 'John', 25), (2, 'Jane', 30)]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
