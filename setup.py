#!/usr/bin/python3

from setuptools import setup, find_packages
import os
import sys
from pytfiles import __version__

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
setup(name='pyfiles',
    version = __version__,
    description = 'Gestion files',
    author = 'Nicolas Boufidjeline',
    author_email = 'nicolas.boufidjeline@gmail.com',
    packages = ['pytfiles'],
    package_dir={'pytfiles':'pytfiles'},
    license = 'MIT',
    install_requires = [],
    provides = ['pytfiles']
)
