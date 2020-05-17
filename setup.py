from setuptools import setup

setup(
    name='apt-prom-exporter',
    version='0.1.2',
    packages=[''],
    url='',
    license='',
    author='Daniel Sendzik',
    author_email='',
    description='',
    install_requires=[
        'prometheus_client',
        'apscheduler',
    ],
    scripts=[
        'bin/apt-prom-exporter'
    ]
)
