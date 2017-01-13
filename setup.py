#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

setup(name='PokeAPI.py',
      py_modules=['PokeAPI'],
      version=version,
      description='Python 3 wrapper for the unofficial PokeAPI',
      author='James Wenzel',
      author_email='wenzel.james.r@gmail.com',
      url='https://github.com/jameswenzel/PokeAPI.py',
      download_url=('http://github.com/jameswenzel/PokeAPI.py/tarball'
                    '{0}'.format(version)),
      license='Apache License 2.0',
      keywords=['pokemon', 'api', 'pokeapi', 'v2'],
      classifiers=[],
      install_requires=['baseapi >= 0.1.0']
      )
