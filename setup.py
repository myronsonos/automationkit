#!/usr/bin/env python

from distutils.core import setup

DEPENDENCIES = [ "netifaces", "paramiko", "psycopg2", "requests", "sqlalchemy", "sqlalchemy_utils", "ssdp" ]

DEPENDENCY_LINKS = []

setup(name='akit',
      version='1.0',
      description='Automation Kit',
      author='Myron Walker',
      author_email='myron.walker@automationmojo.com',
      url='https://automationmojo.com/products/akit',
      packages=[DEPENDENCIES],
      dependency_links=DEPENDENCY_LINKS
     )
