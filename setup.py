import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='apt-prom-exporter',
    version='0.1.2',
    packages=[''],
    url='https://github.com/Alpha200/apt-prom-exporter',
    license='Apache License 2.0',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Daniel Sendzik',
    author_email='daniel@sendzik.eu',
    description='Prometheus exporter for available apt package updates',
    install_requires=[
        'prometheus_client',
        'apscheduler',
    ],
    scripts=[
        'bin/apt-prom-exporter'
    ]
)
