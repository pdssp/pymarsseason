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
# You should have received a copy of the GNU Lesser General Public License
# along with pyMarsSeason.  If not, see <https://www.gnu.org/licenses/>.
"""Project metadata."""
from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution

__name_soft__ = "pymarsseason"
try:
    __version__ = get_distribution(__name_soft__).version
except DistributionNotFound:
    __version__ = "0.0.0"
__title__ = "pyMarsSeason"
__description__ = "Computes the season based on the solar longitude"
__url__ = "https://github.com/pole-surfaces-planetaires/pymarsseason"
__author__ = "Jean-Christophe Malapert"
__author_email__ = "jean-christophe.malapert@cnes.fr"
__license__ = "GNU Lesser General Public License v3"
__copyright__ = (
    "2022, CNES (Jean-Christophe Malapert for Pôle Surfaces Planétaires)"
)
