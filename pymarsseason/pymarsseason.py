# PyMarsSeason - Computes the season based on the solar longitude
# Copyright (C) 2022-2025 - CNES (Jean-Christophe Malapert for PDSSP (Pôle de Données et Services Surfaces Planétaires))
# This file is part of PyMarsSeason <https://github.com/pdssp/pymarsseason>
# SPDX-License-Identifier: Apache-2.0
"""This module contains the library."""
from enum import Enum
from typing import Dict
from typing import Union

from astropy.time import Time
from loguru import logger

from ._version import __name_soft__
from .config import configure_logging
from .marstime import Mars_Ls


class NoValue(Enum):
    def __repr__(self):
        return "<{}.{}>".format(self.__class__.__name__, self.name)


class Season(NoValue):
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"


class Hemisphere(NoValue):
    NORTH = "north"
    SOUTH = "south"


class PyMarsSeason:
    """The library"""

    def __init__(self, *args, **kwargs):
        # pylint: disable=unused-argument
        level = kwargs.get("level", "INFO")
        configure_logging(level=level)

    def convert_ls_to_season(
        self, lsmars: float
    ) -> Dict[Union[Hemisphere, str], Union[Season, float]]:
        """Convert the areocentric longitude of Mars (Ls) to season.

        Args:
            lsmars (float): Solar longitude

        Raises:
            ValueError: Solar longitude must be in [0, 360[

        Returns:
            Dict[Union[Hemisphere, str], Union[Season, float]]: Return the season name for each hemisphere and the solar longitude
        """
        result: Dict[Union[Hemisphere, str], Union[Season, float]] = dict()
        if 0 <= lsmars < 90:
            result = {
                Hemisphere.NORTH: Season.SPRING,
                Hemisphere.SOUTH: Season.AUTUMN,
            }
        elif 90 <= lsmars < 180:
            result = {
                Hemisphere.NORTH: Season.SUMMER,
                Hemisphere.SOUTH: Season.WINTER,
            }
        elif 180 <= lsmars < 270:
            result = {
                Hemisphere.NORTH: Season.AUTUMN,
                Hemisphere.SOUTH: Season.SPRING,
            }
        elif 270 <= lsmars < 360:
            result = {
                Hemisphere.NORTH: Season.WINTER,
                Hemisphere.SOUTH: Season.SUMMER,
            }
        else:
            raise ValueError("Solar longitude must be in [0, 360[")

        result["ls"] = lsmars
        return result

    def compute_season_from_time(
        self, time: Time
    ) -> Dict[Union[Hemisphere, str], Union[Season, float]]:
        """Compute the season from time.

        Args:
            time (Time): TT scale with ISO format

        Raises:
            ValueError: Solar longitude must be in [0, 360[

        Returns:
            Dict[Union[Hemisphere, str], Union[Season, float]]: Return the season name for each hemisphere and the solar longitude
        """
        logger.debug(f"Input: {time}")
        assert isinstance(
            time, Time
        ), "time must have the astropy.time.Time type"
        assert time.scale == "utc", "Time must be in terrestrial time scale"

        # convert to J2000
        deltJ2000 = time.jd - 2451545.0

        lsmars = float(Mars_Ls(deltJ2000))
        logger.debug(f"Solar longitude: {lsmars}")

        season: Dict[Union[Hemisphere, str], Union[Season, float]] = (
            self.convert_ls_to_season(lsmars)
        )
        logger.debug(f"Season in Mars in {time} = {season}")
        return season
