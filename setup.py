"""Crossword solver setup."""

from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Crossword Solver',  # Required
    version='0.0.1',  # Required
    description='Finds all words in a crossword puzzle along the vertical or horizontal axises.',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/toddbirchard/crossword-solver',  # Optional
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Contacts Group',  # Optional
    packages=find_packages(),
    install_requires=['toolz'],
    entry_points={
        'console_scripts': [
            'main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/crossword-solver/issues',
        'Source': 'https://github.com/toddbirchard/crossword-solver/',
    },
)
