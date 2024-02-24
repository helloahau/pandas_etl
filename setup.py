#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Joe",
    author_email='joe@example.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="simple etl",
    entry_points={
        'console_scripts': [
            'pandas_etl=pandas_etl.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pandas_etl',
    name='pandas_etl',
    packages=find_packages(include=['pandas_etl', 'pandas_etl.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/helloahau/pandas_etl',
    version='1.0.0',
    zip_safe=False,
)
