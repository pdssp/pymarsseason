# PyMarsSeason - Computes the season based on the solar longitude
# Copyright (C) 2022-2025 - CNES (Jean-Christophe Malapert for PDSSP (Pôle de Données et Services Surfaces Planétaires))
# This file is part of PyMarsSeason <https://github.com/pdssp/pymarsseason>
# SPDX-License-Identifier: Apache-2.0
"""Computes the season based on the solar longitude"""
from .config import configure_logging

configure_logging()

from ._version import __author__
from ._version import __author_email__
from ._version import __copyright__
from ._version import __description__
from ._version import __license__
from ._version import __name_soft__
from ._version import __title__
from ._version import __url__
from ._version import __version__ as version
from .pymarsseason import PyMarsSeason
from .pymarsseason import Season
from .pymarsseason import Hemisphere
from .pymarsseason import Time

__all__ = ["PyMarsSeason", "version", "Hemisphere", "Season", "Time"]
