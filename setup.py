from setuptools import setup, find_packages

setup(
    name='synthesizer',
    version='0.1',
    license='MIT',
    packages=find_packages(
        where='.',
        include=['synthesizer.*']
    ),
)