.. image:: https://badges.gitter.im/genropy/genropy-core.svg
   :alt: Join the chat at https://gitter.im/genropy/genropy-core
   :target: https://gitter.im/genropy/genropy-core?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Genropy Core
============

Genropy core library (www.genropy.org)

Contributing
------------

We are grateful to the community for contributing bug fixes and
improvements. Read below to learn how you can take part in improving
Genropy. We appreciate your help!

Contribution Guide
~~~~~~~~~~~~~~~~~~

Read our `contribution
guidelines <https://github.com/genropy/genropy-core/blob/master/CONTRIBUTING.md>`__
to learn about our development process, how to propose fixes and
improvements, and how to test your changes before submitting a pull
request.

Development
~~~~~~~~~~~

To setup your development environment, first clone this repo locally:

::

    # Clone source repository:
    git clone https://github.com/genropy/genropy-core.git

Then follow the instructions in one or more of the following sections.

Running tests with tox
^^^^^^^^^^^^^^^^^^^^^^

First, install :code:`tox` with pip in your user install directory (you could run
this inside a virtualenv, and it is the recommended approach, as always):

::

    pip install --user tox

Then, install the binaries for at least Python 2.7 and one or more 3.x versions
(please note that the project supports any Python 3 version starting from 3.4).
For this you are on your own. There are different solutions available for each
major OS (for example, in macOS you could use Conda or MacPorts / Homebrew).

To run tests:

::

    tox

To run only static code analysis checks:

::

    tox -e check

Tox is configured to skip running tests for the Python versions not installed on
your machine.

Setup Environment for Debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To enable debugging, you'll need to install all the needed dependencies in one
virtualenv, created from one of the supported Python versions. To debug the source
under more than one Python version, you'll need to create one virtualenv for each
version.

In the following steps, substitute :code:`path_to_python_interpreter` with the full path
of one of your installed Python binaries, and :code:`venv_name` with a new virtualenv
name. We suggest using some tool to aid in the management of your virtual environments
(for example `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_).

::

    # Create and activate virtual Python environment:
    virtualenv -p <path_to_python_interpreter> <venv_name>
    source <venv_name>/bin/activate
    # Install requirements into virtual environment
    pip install -r requirements-dev.txt

Please note that these steps are not required if you only need to run tests. In that
case follow the steps in the `Running tests with tox
<https://github.com/genropy/genropy-core/blob/master/README.rst#running-tests-with-tox>`__
section.

Original License
----------------

Copyright (c) 2007-2017 Softwell Sas - Milano - Italy

Authors
~~~~~~~

-  Giovanni Porcari
-  Saverio Porcari
-  Francesco Porcari
-  Michele Bertoldi

Licensed under the GNU LGPL License, Version 2.1, see LICENSE file for
details.

Other Contributors (in alphabetical order)
------------------------------------------

-  Paolo Furini
