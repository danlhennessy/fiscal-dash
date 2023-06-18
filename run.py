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

    flask_app.app.run(host="0.0.0.0", port=5000)


def pytest_run():
    pytest.main(args=['--html=report.html'])


if __name__ == "__main__":
    # pytest_thread = Thread(target=pytest_run())
    # pytest_thread.start()

    flask_run()

    # pytest_thread.join()
