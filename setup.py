#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fan_courier_client',
    version='0.2',
    description='Fan Courier Python API Client Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='EBS Integrator',
    author_email='office@ebs-integrator.com',
    url='https://github.com/RodiZaharadji/fan-courier-client',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
    python_requires=">=3.4",
    install_requires=[
        'requests'
    ],
    license='MIT',
)
