import sys
import airflow_utils


def test_ping():
    sys.argv = ['foo', '10']
    airflow_utils.ping()

