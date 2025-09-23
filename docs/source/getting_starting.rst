============
Introduction
============

Purpose
=======

.. automodule:: pymarsseason

Quickstart
==========

Install
-------

Make sure that Python 3.8 (or later) is available, and install the latest version of ``pymarsseason`` using `pip <https://pip.pypa.io>`_\ ,

.. code-block:: shell

    $ pip install git+https://github.com/pole-surfaces-planetaires/pymarsseason.git

Run it
------

You can run it as command line:

.. code-block:: shell

    $ pymarsseason -h

    usage: pymarsseason [-h] [-v] -t TIME [--level {INFO,DEBUG,WARNING,ERROR,CRITICAL,TRACE}]
    Computes the season based on the solar longitude

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -t TIME, --time TIME  UTC time (default: 2021-05-24 12:00:00)
    --level {INFO,DEBUG,WARNING,ERROR,CRITICAL,TRACE}
                            set Level log (default: INFO)

.. code-block:: shell

    $ pymarsseason -t "2022-01-01 00:00:00"

    {<Hemisphere.NORTH>: <Season.SUMMER>, <Hemisphere.SOUTH>: <Season.WINTER>, 'ls': 150.64884820217637}

You can run using the library :

.. code-block:: shell

    $ from pymarsseason import PyMarsSeason, Hemisphere, Season, Time
    $ pyseason = PyMarsSeason()
    $ season1 = pyseason.convert_ls_to_season(180)

    $ time = Time("2021-01-01", format="iso", scale="utc")
    $ season2 = pyseason.compute_season_from_time(time)

Develop it
----------

.. code-block:: shell

    $ git clone https://github.com/pole-surfaces-planetaires/pymarsseason.git
    $ cd pymarsseason
    $ make prepare-dev
    $ source .pymarsseason
    $ make install-dev
