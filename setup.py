#!/usr/bin/env python

from distutils.core import setup
import os


setup(name='Jarvis',
      version='1.0',
      description='Artificial Intelligence for Raspberry Pi',
      author='Sveno Walder',
      author_email='sveno.w@hotmail.com',
      packages=[os.read("requirements.txt").split("\n")],
     )