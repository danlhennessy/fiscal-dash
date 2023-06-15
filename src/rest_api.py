from flask import jsonify
from src import database


def get_all():
    result = database.retrieve_database(
        table="pie_data",
        keys=["id", "user", "category", "value"],
        connection=database.FISCALDB
        )
    return jsonify(result)


def get_users():
    result = database.retrieve_database(
        table="pie_data",
        keys=["user"],
        connection=database.FISCALDB
        )
    return jsonify(result)


def get_key(key):
    result = database.retrieve_database(
        table="pie_data",
        keys=[key],
        connection=database.FISCALDB
        )
    return jsonify(result)


def create_task():
    pass
