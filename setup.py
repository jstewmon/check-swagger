from __future__ import absolute_import

from setuptools import find_packages
from setuptools import setup

setup(
    name='check_swagger',
    description='pre-commit hook for validation swagger specs',
    url='https://github.com/jstewmon/check-swagger',
    version='0.1.2',
    author='Jonathan Stewmon',
    author_email='jstewmon@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
        'PyYAML',
        'swagger_spec_validator',
    ],
    extras_require={
        'dev': [
            'pre-commit',
            'pytest'
        ]
    },
    entry_points={
        'console_scripts': [
            'check-swagger = check_swagger.main:main',
        ],
    },
)
