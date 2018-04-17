#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkgversion import list_requirements, pep440_version, write_setup_py
from setuptools import find_packages

write_setup_py(
    name='katka-api',
    version=pep440_version(),
    description="Katka API",
    long_description=open('README.md').read(),
    author="Claudia Cardoso",
    author_email='claudia.pereirapintocardoso@kpn.com',
    url='https://github.com/kpn/katka-api',
    install_requires=list_requirements('requirements/requirements-base.txt'),
    packages=find_packages(),
    tests_require=['tox'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
