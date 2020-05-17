from prometheus_client import start_http_server, Gauge

from apt_check import run
from typing import NamedTuple
from apscheduler.schedulers.blocking import BlockingScheduler


class Options(NamedTuple):
    security_updates_unattended: bool
    show_package_names: bool
    readable_output: bool


scheduler = BlockingScheduler()

NUM_UPDATES = Gauge('apt_updates', 'Number of available apt updates')
NUM_SECURITY_UPDATES = Gauge('apt_security_updates', 'Number of available apt security updates')


def check_apt():
    options = Options(False, False, False)
    (num_updates, num_security_updates) = run(options)
    NUM_UPDATES.set(num_updates)
    NUM_SECURITY_UPDATES.set(num_security_updates)


if __name__ == '__main__':
    check_apt()

    # Start up the server to expose the metrics.
    start_http_server(8000)

    scheduler.add_job(check_apt, 'interval', hours=12)
    scheduler.start()
