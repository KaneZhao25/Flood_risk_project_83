# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.unit_test_stations import build_unit_test_stations
from haversine import haversine

def test_relative_water_level():
    stations = build_station_list()
    update_water_levels(stations)
    stations_over_threshold = stations_level_over_threshold(stations)
    assert isinstance(stations_over_threshold[0][0], MonitoringStation)
    assert isinstance(stations_over_threshold[0][1], float)
    assert sorted_by_key(stations_over_threshold, 1, reverse=True) == stations_over_threshold

def test_unit_stations_relative():
    unit_stations = build_unit_test_stations()
    unit_stations_over_threshold = stations_level_over_threshold(unit_stations)
    assert len(unit_stations_over_threshold) == 1
    assert unit_stations_over_threshold[0][0].name == 'Test Station 4'
    assert unit_stations_over_threshold[0][0].relative_water_level() == 1.0