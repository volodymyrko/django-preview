#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-preview',
    version="0.1",
    author='Kovtun Volodymyr',
    author_email='vova-zms@yandex.ua',
    description='Managing preview subscription in Django',
    long_description = 'Managing preview subscription in Django, with email notification, and unsubscription support',
    url='https://github.com/volodymyrko/django-preview',
    download_url='https://github.com/volodymyrko/django-preview',
    license = 'BSD',
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
