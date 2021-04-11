#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyicnsim',
    version='1.1',
    author='Ryo Nakamura',
    author_email='nakamura@zebulun.net',
    description='ICN (Information-Centric Networking) SIMulator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/r-nakamura/pyicnsim",
    packages=setuptools.find_packages(),
    install_requires=['perlcompat', 'graph_tools'],
    scripts=['bin/pyicnsim'],
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: OS Independent',
    ],
)
