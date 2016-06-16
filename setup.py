#!/usr/bin/env python

import sys
from setuptools import setup


install_requires = [
    'newspaper3k>=0.1.7',
    'click>=6.6',
    'jinja2>=2.8',
    'awesome-slugify>=1.6.5'
]

setup(
    name = "merle",
    version='0.0.2.2',
    description='Command-line tool for extracting metadata from URLs',
    long_description='Yada',
    author='Dan Nguyen',
    author_email='dansonguyen@gmail.com',
    url='https://github.com/dannguyen/merle',
    license='MIT',
    classifiers=[
            'Programming Language :: Python :: 3.4',
            'Environment :: Console',
            'Intended Audience :: Developers'
    ],
    packages=['merle'],
    package_data={
        'jinja templates': 'merle/templates/*.txt',
        'data': 'merle/data/*.txt'},
    entry_points={
        'console_scripts': ['merle = merle.cli:fetch_metadata']
    },
    install_requires = install_requires
)
