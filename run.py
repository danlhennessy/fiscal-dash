from src import flask_app, database
import logging
import pytest
from threading import Thread


def flask_run():
    database.check_mysql_connection(database.FISCALDB)

    debug_mode = False
    flask_app.app.debug = debug_mode

    # log_file = 'logs/app.log'
    # log_level = logging.DEBUG if debug_mode else logging.INFO
    # logging.basicConfig(filename=log_file, level=log_level)

    flask_app.app.run(host='0.0.0.0')


def run_pytest():
    pytest.main()


if __name__ == "__main__":
    # flask_thread = Thread(target=flask_run)
    # flask_thread.start()

    # pytest_thread = Thread(target=run_pytest)
    # pytest_thread.start()

    # pytest_thread.join()
    
    flask_run()