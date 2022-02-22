# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold 
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.unit_test_stations import build_unit_test_stations
from haversine import haversine

def test_relative_water_level():
    stations = build_station_list()
    update_water_levels(stations)
    stations_most_at_risk = stations_highest_rel_level(stations, 10)
    stations_tuple = [(i.name, i.relative_water_level()) for i in stations_most_at_risk]
    assert isinstance(stations_most_at_risk[0], MonitoringStation)
    assert sorted_by_key(stations_tuple, 1, reverse=True) == stations_tuple
    

