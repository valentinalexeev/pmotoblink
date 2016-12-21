#!/usr/bin/env python

from distutils.core import setup

setup(name='pmotoblink',
	version='1.0',
	description='Python interface to Motorola Blink-like cameras',
	author='Valentin Alexeev',
	author_email='valentin.alekseev@gmail.com',
	url='https://github.com/valentinalexeev/pmotoblink',
	packages=['pmotoblink'],
	install_requires=['requests']
)