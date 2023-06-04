from src import app_config
import mysql.connector

FISCALDB = mysql.connector.connect(
    host='localhost',
    user=app_config.DB_USER,
    password=app_config.DB_PASS,
    database=app_config.DB_NAME
)


def retrieve_database(table: str,
                      keys: list[str],
                      connection: mysql.connector.MySQLConnection):
    cursor = connection.cursor()
    query = f"SELECT {', '.join(keys)} FROM {table}"
    cursor.execute(query)
    return cursor.fetchall()


def update_database(table: str,
                    keys: list[str],
                    values: list[str],
                    connection: mysql.connector.MySQLConnection):
    try:
        cursor = connection.cursor()
        placeholders = ','.join(['%s'] * len(keys))
        query = f"INSERT INTO {table} ({','.join(keys)}) VALUES ({placeholders})"
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
    except ValueError as updateDB_error:
        print(f"Error: {updateDB_error}")