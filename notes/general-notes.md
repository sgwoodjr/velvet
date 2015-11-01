General Notes
=============

* Should the validation module be exposed to the top level API, or
  should it be kept private for internal use?

  - If it is kept private, then the function names should be prepended
    with an underscore.

* What is the best method of properly using git tags with a PGP key?

* Establish the documentation approach

## Anaconda
$ source activate <environment>
$ source deactivate

## Submit a PyPI Package

This assumes the ~/.pypirc file is configured.

* Test site
  $ python setup.py register -r pypitest
  $ python setup.py sdist upload -r pypitest

* Live site
  $ python setup.py register -r pypi
  $ python setup.py sdist upload -r pypi
