#-*- coding:utf-8 -*-

import setuptools
from enginehub import sphinx_youtube as pkg

setuptools.setup(
    name='enginehub.sphinx_youtube',
    version=pkg.__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'sphinx'
        ],
    author=pkg.__author__,
    license=pkg.__license__,
    url='https://github.com/EngineHub/sphinxcontrib.youtube',
    description='''embedding gist to sphinx''',
    long_description=pkg.__doc__,
    namespace_packages=['enginehub'],
    classifiers='''
Programming Language :: Python
Development Status :: 4 - Beta
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Topic :: Software Development :: Documentation
'''.strip().splitlines())

