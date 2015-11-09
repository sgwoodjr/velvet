General Notes
=============

* Should the validation module be exposed to the top level API, or
  should it be kept private for internal use?

  - If it is kept private, then the function names should be prepended
    with an underscore.

* What is the best method of properly using git tags with a PGP key?

## Documenation

Here are some general thoughts. They will get refined as time goes on.

* Generally, we should follow the Numpy documentation standard. But,
there are some things I don't particularly care for

  - I don't like the tick marks surrounding parameter names. For
  example, `x`. I find it cumbersome when reading.

  - I mostly read the documentation at the command line using either
  'help(foo)' or from IPython with 'foo?'. As such, the mathematical
  equations using Latex should be kept at a minimum. The equations look
  great in a web page or printed pdf, but it sucks having to read
  through the crud at the terminal.

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

## Adding new functionality to Velvet
 
* Add proper error checking to input values
  - Each function will work with a scalar or ndarray. For ndarrays,
  decide on the proper dimension that will be supported and verify it.
* Add proper documentation
* Add unit tests
* If it's a new module, don't forget to update __init__.py 
* Add the new function or class to the module API

## IPython

* Reload a module
  - $ In [15]: %reload_ext <module name>

// vim: set syntax=markdown:
