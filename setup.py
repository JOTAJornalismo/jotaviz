#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

import jotaviz

VERSION = jotaviz.__version__

with open('README.md') as readme_file:
    README = readme_file.read()

INSTALL_REQUIRES = ['matplotlib',
                    'pandas',
                    'scipy',
                    'atexit',
                    'pillow',
                    'numpy',
                    ]

# Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT License',
               'Operating System :: OS Independent',
			   'Framework :: Matplotlib',
               'Programming Language :: Python :: 3 :: Only',
               'Topic :: Scientific/Engineering/Journalism :: Visualization']


setup(name='jotaviz',
      version=VERSION,
      description='A Python package for data visualization styles and plots used at https://jota.info',
      long_description_content_type="text/markdown",
      long_description=README,
      classifiers=CLASSIFIERS,
      url='https://github.com/JOTAJornalismo/jotaviz/',
      author='Daniel Marcelino',
      author_email='daniel.marcelino@jota.info',
      author_twitter='@dmarcelinobr',
      license='MIT',
      packages=['jotaviz'],
      python_requires='>=3.6',
      install_requires=INSTALL_REQUIRES,
      zip_safe=False)
