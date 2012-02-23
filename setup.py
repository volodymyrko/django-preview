#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-preview',
    version="0.1",
    author='Kovtun Volodymyr',
    author_email='vova-zms@yandex.ua',
    description='Managing preview subsciprion in Django',
    url='',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
