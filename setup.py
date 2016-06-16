#!/usr/bin/env python

import sys
from setuptools import setup


install_requires = [
    'newspaper3k>0.1.7',
    'click>=6.6',
    'rtyaml>=0.0.3',
    'awesome-slugify>=1.6.5'
]


setup(
    name = "merle",
    version='0.0.1',
    description='Command-line tool for extracting metadata from URLs',
    long_description='Yada',
    author='Dan Nguyen',
    author_email='dansonguyen@gmail.com',
    url='http://danwin.com',
    license='MIT',
    classifiers=['Whoa :: Dude'],
    packages=['merle'],
    entry_points={
        'console_scripts': ['merle = merli.cli']
    },
    install_requires = ['merle']
)
