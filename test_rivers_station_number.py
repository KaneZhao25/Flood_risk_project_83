# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
"""Unit test for the river by station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation
from test_fake_station_list import fake_station_list

def test_river():
    stations = fake_station_list()
    river_test_list = rivers_by_station_number(stations, 2)
    assert len(river_test_list) == 3
    assert river_test_list == ([('River D', 3), ('River C', 2), ('River B', 2)] or [('River D', 3), ('River B', 2), ('River C', 2)])
