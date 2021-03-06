#!/usr/bin/env python

"""
Set up for XBlock
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import codecs
import os.path
from setuptools import setup

VERSION_FILE = os.path.join(os.path.dirname(__file__), 'xblock/VERSION.txt')

setup(
    name='XBlock',
    version=codecs.open(VERSION_FILE, encoding='ascii').read().strip(),
    description='XBlock Core Library',
    packages=[
        'xblock',
        'xblock.django',
        'xblock.reference',
        'xblock.test',
        'xblock.test.django',
    ],
    include_package_data=True,
    install_requires=[
        'fs',
        'lxml',
        'markupsafe',
        'python-dateutil',
        'pytz',
        'pyyaml',
        'six',
        'webob',
        'web-fragments',
    ],
    extras_require={
        'django': ['django-pyfs >= 1.0.5']
    },
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ]
)
