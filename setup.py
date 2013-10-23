#!/usr/bin/env python
# -*- coding: utf-8  -*-
################################################################################
#
#  sqlalchemy-pervasive -- SQLAlchemy Dialect for Pervasive PSQL
#  Copyright © 2013 Sacramento Natural Foods Co-op, Inc
#
#  This file is part of sqlalchemy-pervasive.
#
#  sqlalchemy-pervasive is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by the
#  Free Software Foundation, either version 3 of the License, or (at your
#  option) any later version.
#
#  sqlalchemy-pervasive is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  sqlalchemy-pervasive.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################


import os.path
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
execfile(os.path.join(here, 'sqlalchemy_pervasive', '_version.py'))

README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()


requires = [
    #
    # Version numbers within comments below have specific meanings.
    # Basically the 'low' value is a "soft low," and 'high' a "soft high."
    # In other words:
    #
    # If either a 'low' or 'high' value exists, the primary point to be
    # made about the value is that it represents the most current (stable)
    # version available for the package (assuming typical public access
    # methods) whenever this project was started and/or documented.
    # Therefore:
    #
    # If a 'low' version is present, you should know that attempts to use
    # versions of the package significantly older than the 'low' version
    # may not yield happy results.  (A "hard" high limit may or may not be
    # indicated by a true version requirement.)
    #
    # Similarly, if a 'high' version is present, and especially if this
    # project has laid dormant for a while, you may need to refactor a bit
    # when attempting to support a more recent version of the package.  (A
    # "hard" low limit should be indicated by a true version requirement
    # when a 'high' version is present.)
    #
    # In any case, developers and other users are encouraged to play
    # outside the lines with regard to these soft limits.  If bugs are
    # encountered then they should be filed as such.
    #
    # package                           # low                   high

    'pyodbc',                           # 2.1.11
    'SQLAlchemy',                       # 0.8.2
    ]


setup(
    name = "sqlalchemy-pervasive",
    version = __version__,
    author = "Sacramento Natural Foods Co-op, Inc",
    author_email = "developer@sacfoodcoop.com",
    license = "GNU GPL v3",
    description = "SQLAlchemy Dialect for Pervasive PSQL",
    long_description = README + '\n\n' +  CHANGES,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

    install_requires = requires,
    packages = find_packages(exclude=['tests']),
    include_package_data = True,

    entry_points = """

[sqlalchemy.dialects]
pervasive = sqlalchemy_pervasive.pyodbc:PervasiveDialect_pyodbc

""",
    )
