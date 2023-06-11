from src import flask_app, database
import logging
import pytest
from threading import Thread


def flask_run():
    debug_mode = False
    flask_app.app.debug = debug_mode

    # log_file = 'logs/app.log'
    # log_level = logging.DEBUG if debug_mode else logging.INFO
    # logging.basicConfig(filename=log_file, level=log_level)

    flask_app.app.run(host='0.0.0.0')


if __name__ == "__main__":

    database.check_mysql_connection(database.FISCALDB)

    flask_thread = Thread(target=flask_run)
    flask_thread.start()

    pytest.main()

    flask_thread.join()
