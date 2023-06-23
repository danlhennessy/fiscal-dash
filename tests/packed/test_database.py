import unittest
import mysql.connector
import os
from src.vault_actions import FISCAL_VAULT

fiscal_dict = FISCAL_VAULT.dict_all('secret')

if os.environ.get('DOCKER_ENV') == 'true':
    database_host = fiscal_dict['AWS_DB_HOST']
    database_user = fiscal_dict['AWS_DB_USER']
    database_port = '3306'
else:
    database_host = fiscal_dict['AWS_DB_HOST']
    database_user = fiscal_dict['AWS_DB_USER']
    database_port = '30007'


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = mysql.connector.connect(
            host=database_host,
            port=database_port,
            user=database_user,
            password=fiscal_dict['DB_PASS'],
            database=fiscal_dict['DB_NAME']
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
