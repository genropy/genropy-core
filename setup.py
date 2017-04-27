import os
import sys
from setuptools import setup, find_packages


_local_dir = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    abs_path = os.path.join(_local_dir, filename)
    with open(abs_path, mode='rt') as f:
        return f.read()


about = {}
exec(read_file(os.path.join('gnr', '__about__.py')), about)

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []


setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__email__'],
    description=about['__summary__'],
    url=about['__uri__'],
    license=about['__license__'],
    long_description=read_file('README.rst'),
    packages=find_packages(),

    setup_requires=[
        # Environment markers were implemented and stabilized in setuptools
        # v20.8.1 (see <http://stackoverflow.com/a/32643122/391865>).
        'setuptools>=20.8.1',
        # If line above doesn't work, check that you have at least
        # setuptools v19.4 (released 2016-01-16):
        # <https://github.com/pypa/setuptools/issues/141>
    ] + pytest_runner,
    tests_require=['pytest'],
    test_suite='tests',

    install_requires=[
        'pytz',
        'babel',
        'future',
        'python-dateutil',
    ],
    zip_safe=True,

    classifiers=[
        'Development Status ::  3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Genropy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
