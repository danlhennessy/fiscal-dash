import unittest
import mysql.connector
import tests.test_config as test_config


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user=test_config.DB_USER,
            password=test_config.DB_PASS,
            database=test_config.DB_NAME
        )
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
