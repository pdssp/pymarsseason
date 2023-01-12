# -*- coding: utf-8 -*-
"""This module contains the library."""
import configparser
import logging
from enum import Enum
from typing import Dict
from typing import Union

import marstime
from astropy.time import Time

from ._version import __name_soft__

logger = logging.getLogger(__name__)


class NoValue(Enum):
    def __repr__(self):
        return "<%s.%s>" % (self.__class__.__name__, self.name)


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
        if "level" in kwargs:
            PyMarsSeason._parse_level(kwargs["level"])

    @staticmethod
    def _parse_level(level: str):
        """Parse level name and set the rigt level for the logger.
        If the level is not known, the INFO level is set

        Args:
            level (str): level name
        """

        if level == "INFO":
            logger.setLevel(logging.INFO)
        elif level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif level == "WARNING":
            logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
        elif level == "TRACE":
            logger.setLevel(logging.TRACE)  # type: ignore # pylint: disable=no-member
        else:
            logger.warning(
                "Unknown level name : %s - setting level to INFO", level
            )
            logger.setLevel(logging.INFO)

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

        lsmars = marstime.Mars_Ls(deltJ2000)
        logger.debug(f"Solar longitude: {lsmars}")

        season: Dict[
            Union[Hemisphere, str], Union[Season, float]
        ] = self.convert_ls_to_season(lsmars)
        logger.debug(f"Season in Mars in {time} = {season}")
        return season
