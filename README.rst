|Travis| |Coveralls| |PyPI Version| |PyPI Downloads| |PyPI Python Versions|

Velvet
======

*"That's beautiful, what is that velvet?"*

    .. note:: This project is still in the planning phase. The foundation of
    the project is still being configured. Once that is complete, actual
    signal processing functionality will be added.


Velvet provides signal processing and communications algorithms in
Python. Typical usage often looks like this::

    #!/usr/bin/env python

    import velvet as vt

Install
-------
Requirements/Dependencies

- Python 2.7 or above
- NumPy 1.7 or above
- SciPy 0.13 or above
- Matplotlib 1.3.1 or above

The package is available on
`PyPI <https://pypi.python.org/pypi/velvet>`__:

::

    $ pip install velvet

To get the latest development work, clone from github and install as follows::

    $ git clone https://github.com/sgwoodjr/velvet.git
    $ cd velvet
    $ python setup.py install

Unit testing::

   $ nosetests -v

Run unit tests with a coverage report::

   $ nosetests -v --with-coverage --cover-html --cover-package=velvet

Contribute
----------
| Write a bug report or send a pull request.
| Here is what others have done
  `contributors <https://github.com/sgwoodjr/velvet/graphs/contributors>`__
  
License
-------

| Copyright (c) 2015 SGW
| The source code is available under the **New BSD License**.
| See
  `LICENSE <https://github.com/sgwoodjr/velvet/blob/master/LICENSE>`__
  for further details.
  
.. |Coveralls| image:: https://img.shields.io/coveralls/sgwoodjr/velvet.svg
   :target: https://coveralls.io/github/sgwoodjr/velvet?branch=master
.. |Travis| image:: https://travis-ci.org/sgwoodjr/velvet.svg?branch=master
   :target: https://travis-ci.org/sgwoodjr/velvet
.. |PyPI Version| image:: https://img.shields.io/pypi/v/velvet.svg
   :target: https://pypi.python.org/pypi/velvet
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/velvet.svg
   :target: https://pypi.python.org/pypi/velvet
.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/velvet.svg
   :target: https://pypi.python.org/pypi/velvet
