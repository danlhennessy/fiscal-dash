"""Connects to Fiscal DB and provides functions for database utility:
Retrieving, updating values"""
import mysql.connector
from src import app_config


class MySQLConnectionError(Exception):
    """Custom exception for errors encountered during MySQL DB connection"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"MySQL Connection Error: {self.message}"


FISCALDB = mysql.connector.connect(
    host='localhost',
    user=app_config.DB_USER,
    password=app_config.DB_PASS,
    database=app_config.DB_NAME
)


def check_mysql_connection(connection):
    """Confirms database link on connection, displays any errors"""
    try:
        connection.ping(reconnect=True)
        print("MySQL connection successful")
    except MySQLConnectionError as error:
        print("Error connecting to MySQL database:", str(error))


def retrieve_database(table: str,
                      keys: list[str],
                      connection: mysql.connector.MySQLConnection):
    """Gets database table values from provided keys"""
    cursor = connection.cursor()
    query = f"SELECT {', '.join(keys)} FROM {table}"
    cursor.execute(query)
    return cursor.fetchall()


def update_database(table: str,
                    keys: list[str],
                    values: list,
                    connection: mysql.connector.MySQLConnection):
    """Updates database table with provided key/values"""
    try:
        cursor = connection.cursor()
        placeholders = ','.join(['%s'] * len(keys))
        query = f"INSERT INTO {table} ({','.join(keys)}) VALUES ({placeholders})"
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
    except ValueError as updatedb_error:
        print(f"Error: {updatedb_error}")
