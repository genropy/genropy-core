from __future__ import print_function
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages
import sys
import os


_local_dir = os.path.abspath(os.path.dirname(__file__))


#
# http://pytest.org/dev/goodpractises.html
#   #integration-with-setuptools-test-commands
#
class RunTests(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--verbose', '--strict', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


#
# pull_request #5
readme_rst_path = os.path.join(_local_dir, 'README.rst')
if os.path.isfile(readme_rst_path):
    long_description = open(readme_rst_path)
else:
    long_description = open(os.path.join(_local_dir, 'README.md'))


setup(
    name='Genropy-core',
    version='0.0.1',
    url='http://www.genropy.org/',
    author='Genropy',
    author_email='info@genropy.org',
    description=('''An insanely fast way to create
 Single Page Applications in python. Core package'''),
    long_description=long_description,
    license='LGPL',

    tests_require=['pytest'],
    cmdclass={'test': RunTests},

    packages=find_packages(),
    # install_requires=['...']
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
