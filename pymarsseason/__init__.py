# -*- coding: utf-8 -*-
# pyMarsSeason - Computes the season based on the solar longitude
# Copyright (C) 2022 - CNES (Jean-Christophe Malapert for Pôle Surfaces Planétaires)
#
# This file is part of pyMarsSeason.
#
# pyMarsSeason is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License v3  as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyMarsSeason is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License v3  for more details.
#
# You should have received a copy of the GNU Lesser General Public License v3
# along with pyMarsSeason.  If not, see <https://www.gnu.org/licenses/>.
"""The aim of this tool is to provide a simple interface to compute the season
on Mars from a solar longitude or date in UTC.

To see the relationship between season and solar longitude,
`see the following site <http://www-mars.lmd.jussieu.fr/mars/time/solar_longitude.html>`_.

"""
import logging.config
import os
from logging import debug
from logging import getLogger
from logging import NullHandler
from logging import setLogRecordFactory
from logging import warning

from astropy.time import Time

from ._version import __author__
from ._version import __author_email__
from ._version import __copyright__
from ._version import __description__
from ._version import __license__
from ._version import __name_soft__
from ._version import __title__
from ._version import __url__
from ._version import __version__
from .custom_logging import LogRecord
from .custom_logging import UtilsLogs
from .pymarsseason import Hemisphere
from .pymarsseason import PyMarsSeason
from .pymarsseason import Season

getLogger(__name__).addHandler(NullHandler())

UtilsLogs.add_logging_level("TRACE", 15)
try:
    PATH_TO_CONF = os.path.dirname(os.path.realpath(__file__))
    logging.config.fileConfig(
        os.path.join(PATH_TO_CONF, "logging.conf"),
        disable_existing_loggers=False,
    )
    debug(f"file {os.path.join(PATH_TO_CONF, 'logging.conf')} loaded")
except Exception as exception:  # pylint: disable=broad-except
    warning(f"cannot load logging.conf : {exception}")
setLogRecordFactory(LogRecord)  # pylint: disable=no-member

__all__ = ["Time", "Season", "Hemisphere", "PyMarsSeason"]
