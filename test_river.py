# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
"""Unit test for the river list module"""

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation
from test_fake_station_list import fake_station_list

def test_river():
    stations = fake_station_list()
    river_set = []
    for element in rivers_with_station(stations):
        river_set.append(element)
    assert len(river_set) == 4
