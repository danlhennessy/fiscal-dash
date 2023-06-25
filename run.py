from src import flask_app, database
import pytest
from threading import Thread, local


def flask_run():
    # if getattr(local_data, 'PYTEST_THREAD', True):
    #     print('main thread')
    database.check_mysql_connection(database.FISCALDB)

    debug_mode = False
    flask_app.app.debug = debug_mode

    # host ="0.0.0.0" is required for Flask app to accept connections from K8s
    flask_app.app.run(host="0.0.0.0", port=5000)


def pytest_run():
    # if getattr(local_data, 'PYTEST_THREAD', True):
    #     print('pytest thread')
    pytest.main(args=['--html=logs/report.html'])


if __name__ == "__main__":
    # local_data = local()
    # local_data.PYTEST_THREAD = True
    # pytest_thread = Thread(target=pytest_run())
    # pytest_thread.start()

    flask_run()

    # pytest_thread.join()
