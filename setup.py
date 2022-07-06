from setuptools import setup, find_packages

setup(
    name='synthesizer_and_metallophone',
    version='0.1',
    license='MIT',
    packages=find_packages(
        where='.',
        include=['midi_to_music_sheet.*', 'metallophono.*', 'synthesizer.*']
    ),
)