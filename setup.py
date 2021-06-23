#!/usr/bin/env python3

from setuptools import setup, find_packages

VERSION = '0.0.27'

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()


setup(
    name='bewgor',
    version=VERSION,
    description='Wordlist Generator',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords=['wordlist', 'dictionary-attack'],
    author='berzerk0',
    url='https://github.com/berzerk0/BEWGor',
    license='GPL3',
    classifiers = [
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'bewgor = bewgor.BEWGor:main',
        ],
    }
)
