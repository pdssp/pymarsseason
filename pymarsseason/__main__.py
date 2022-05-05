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
"""Main program."""
import argparse
import signal
import sys
from logging import error
from logging import exception
from logging import getLogger
from typing import Dict
from typing import Union

from astropy.time import Time

from .pymarsseason import Hemisphere
from .pymarsseason import PyMarsSeason
from .pymarsseason import Season
from pymarsseason import __author__
from pymarsseason import __copyright__
from pymarsseason import __description__
from pymarsseason import __version__


class SmartFormatter(argparse.HelpFormatter):
    """Smart formatter for argparse - The lines are split for long text"""

    def _split_lines(self, text, width):
        if text.startswith("R|"):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(  # pylint: disable=protected-access
            self, text, width
        )


class SigintHandler:  # pylint: disable=too-few-public-methods
    """Handles the signal"""

    def __init__(self):
        self.SIGINT = False  # pylint: disable=invalid-name

    def signal_handler(self, sig: int, frame):
        """Trap the signal

        Args:
            sig (int): the signal number
            frame: the current stack frame
        """
        # pylint: disable=unused-argument
        error("You pressed Ctrl+C")
        self.SIGINT = True
        sys.exit(2)


def str2bool(string_to_test: str) -> bool:
    """Checks if a given string is a boolean

    Args:
        string_to_test (str): string to test

    Returns:
        bool: True when the string is a boolean otherwise False
    """
    return string_to_test.lower() in ("yes", "true", "True", "t", "1")


def parse_cli() -> argparse.Namespace:
    """Parse command line inputs.

    Returns
    -------
    argparse.Namespace
        Command line options
    """
    parser = argparse.ArgumentParser(
        description=__description__,
        formatter_class=SmartFormatter,
        epilog=__author__ + " - " + __copyright__,
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )

    parser.add_argument(
        "-t",
        "--time",
        type=str,
        required=True,
        default="2021-05-24 12:00:00",
        help="UTC time (default: %(default)s)",
    )

    parser.add_argument(
        "--level",
        choices=[
            "INFO",
            "DEBUG",
            "WARNING",
            "ERROR",
            "CRITICAL",
            "TRACE",
        ],
        default="INFO",
        help="set Level log (default: %(default)s)",
    )

    return parser.parse_args()


def run():
    """Main function that instanciates the library."""
    handler = SigintHandler()
    signal.signal(signal.SIGINT, handler.signal_handler)
    try:
        options_cli = parse_cli()

        pymarsseason = PyMarsSeason(
            level=options_cli.level,
        )
        time = Time(options_cli.time, format="iso", scale="utc")
        season: Dict[
            Union[Hemisphere, str], Union[Season, float]
        ] = pymarsseason.compute_season_from_time(time)
        print(season)
        sys.exit(0)
    except Exception as error:  # pylint: disable=broad-except
        exception(error)
        sys.exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    run()
