#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages

DEPENDENCIES = [ "coverage", "ipython", "netifaces", "paramiko", "psycopg2", "requests", "SQLAlchemy", "sqlalchemy_utils", "ssdp", "pyyaml", "dlipower", ]

DEPENDENCY_LINKS = []

setup(name='akit',
      version='1.0',
      description='Automation Kit',
      author='Myron Walker',
      author_email='myron.walker@automationmojo.com',
      url='https://automationmojo.com/products/akit',
      package_dir={'': 'packages'},
      package_data={'': ['*.html']},
      packages=find_namespace_packages(where='packages'),
      install_requires=DEPENDENCIES,
      dependency_links=DEPENDENCY_LINKS
     )
