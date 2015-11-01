.. image:: http://img.shields.io/badge/benchmarked%20by-asv-green.svg?style=flat
   :target: https://github.com/sgwoodjr/velvet/

Velvet Benchmarks
=================

Benchmarking Velvet with Airspeed Velocity.

Philosophy
----------

I have not decided on an overall benchmarking approach, or if it is even
necessary for that matter. However, I came across Airspeed Velocity and
it looks pretty slick. This is an attempt to lay down an initial
framework for future use.

Usage
-----

Run ASV commands, record the results and generate HTML::

    cd benchmarks
    asv run
    asv publish
    asv preview

Find out more about ``asv`` by reading the `ASV documentation`_.

.. _ASV documentation: https://spacetelescope.github.io/asv/
