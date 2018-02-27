import os
from distutils.core import setup
from setuptools import find_packages

__author__ = 'Evgeny Tatarintsev'
__version__ = '0.2'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='advcash-api-client',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/evtatarintsev/advcash-api-client',
    license='MIT',
    author=__author__,
    author_email='evtatarintsev@ya.ru',
    keywords=['advcash', 'api', 'client'],
    description='Integrating django project with yandex-money',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'zeep>=2.5.0',
    ],
)
