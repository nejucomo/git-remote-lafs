#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='git-remote-lafs',
    description='Push and pull git repositories into transparently laid out tahoe-lafs storage.',
    version='0.1.dev0',
    author='Nathan Wilcox',
    author_email='nejucomo@gmail.com',
    license='GPLv3',
    url='https://github.com/nejucomo/git-remote-lafs',

    packages=find_packages(),

    entry_points = {
        'console_scripts': [
            'git-remote-lafs = lafsgit.main:main',
            ],
        },

    install_requires = [
        'twisted >= 14.0',
        ],
    )
