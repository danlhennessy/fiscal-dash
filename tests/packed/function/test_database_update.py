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


def update_database(keys: list,
                    values: list,
                    connection: mysql.connector.MySQLConnection):
    """Updates database table with provided key/values"""
    try:
        cursor = connection.cursor()

        placeholders = ','.join(['%s'] * len(keys))
        escaped_keys = [connection._cmysql.escape_string(key) for key in keys]
        clean_keys = [key.decode('utf-8') for key in escaped_keys]

        query = f"INSERT INTO test_table ({','.join(clean_keys)}) VALUES ({placeholders})"

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
    except ValueError as updatedb_error:
        print(f"Error: {updatedb_error}")


class TestUpdateDatabase(TestDatabase):
    def test_retrieve_database(self):
        update_database(
            ["id", "name", "age"],
            [1, "Dan", 30],
            self.connection
            )

        result = retrieve_database(self.connection)

        expected_result = [(1, 'Dan', 30)]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
