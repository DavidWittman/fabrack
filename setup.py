#!/usr/bin/env python

from setuptools import setup, find_packages

__author__ = "David Wittman"
NAME = "fabrack"
DESC = "Rackspace Cloud Servers task library for Fabric",
VERSION = '0.1'

requires = [ 
     'fabric', 
     'python-novaclient == 2.6.0', # novaclient version 2.6.0 has the v1 code
     'python-cloudlb'
     ]

setup(
      name = NAME,
      description = DESC,
      version = VERSION,
      author = __author__,
      author_email = "david@wittman.com",
      license = "BSD",

      packages = find_packages('src'),
      package_dir = { '' : 'src' },
      install_requires = requires,
      zip_safe = True,
      classifiers = [
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        ]
      )
