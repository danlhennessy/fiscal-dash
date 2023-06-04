import unittest
import mysql.connector
import tests.test_config as test_config
from src.app import retrieve_database


class TestRetrieveDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user=test_config.DB_USER,
            password=test_config.DB_PASS,
            database=test_config.DB_NAME
        )
        # Create a test table
        self.create_test_table()

    def tearDown(self):
        self.drop_test_table()
        self.connection.close()

    def create_test_table(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "CREATE TABLE test_table (id INT, name VARCHAR(255), age INT)"
            )

    def drop_test_table(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE test_table")

    def test_retrieve_database(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO test_table (id, name, age) VALUES (1, 'John', 25)"
            )
        cursor.execute(
            "INSERT INTO test_table (id, name, age) VALUES (2, 'Jane', 30)"
            )
        self.connection.commit()

        result = retrieve_database(
            "test_table",
            ["id", "name"],
            self.connection
            )

        expected_result = [(1, 'John'), (2, 'Jane')]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
