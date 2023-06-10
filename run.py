from src import flask_app, database
import logging

if __name__ == "__main__":
    database.check_mysql_connection(database.FISCALDB)

    debug_mode = False
    flask_app.app.debug = debug_mode

    # log_file = 'logs/app.log'
    # log_level = logging.DEBUG if debug_mode else logging.INFO
    # logging.basicConfig(filename=log_file, level=log_level)

    flask_app.app.run()
