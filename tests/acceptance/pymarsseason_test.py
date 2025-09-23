import pytest

from pymarsseason import Hemisphere
from pymarsseason import PyMarsSeason
from pymarsseason import Season
from pymarsseason import Time


def test_season_from_ls_0():
    pyseason = PyMarsSeason()
    season = pyseason.convert_ls_to_season(0)
    assert season[Hemisphere.NORTH] == Season.SPRING


def test_season_from_ls_90():
    pyseason = PyMarsSeason()
    season = pyseason.convert_ls_to_season(90)
    assert season[Hemisphere.NORTH] == Season.SUMMER


def test_season_from_ls_180():
    pyseason = PyMarsSeason()
    season = pyseason.convert_ls_to_season(180)
    assert season[Hemisphere.NORTH] == Season.AUTUMN


def test_season_from_ls_270():
    pyseason = PyMarsSeason()
    season = pyseason.convert_ls_to_season(270)
    assert season[Hemisphere.NORTH] == Season.WINTER


def test_season_from_time():
    pyseason = PyMarsSeason()
    time = Time("2021-01-01", format="iso", scale="utc")
    season = pyseason.compute_season_from_time(time)
    assert season[Hemisphere.NORTH] == Season.WINTER
    assert season[Hemisphere.SOUTH] == Season.SUMMER
    assert season["ls"] == pytest.approx(340.701627, abs=1e-6)
