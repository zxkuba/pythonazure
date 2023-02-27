#!/usr/bin/env python

import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig

from setuptools import setup
from setuptools import setup, find_packages

class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

setup(
    name='jfrog-python-example',
    version='1.0',
    description='Project example for building Python project with Artifactory',
    author='jakub',
    author_email='jakub@jakub.com',
    url='https://bosch.visualstudio.com/BoschDevelopmentCloud/_git/BDC',
    packages=find_packages(),
    install_requires=['PyYAML>3.11', 'nltk'],
    cmdclass={
        'register': register,
        'upload': upload,
    }
)