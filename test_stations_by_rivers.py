# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation
from test_fake_station_list import fake_station_list

def test_station_list():
    stations = fake_station_list()
    def print_station_name(river):
        river_dic = stations_by_river(stations)
        stations_on_river = []
        stations_on_river.append(river_dic[river])
        stations_on_river.sort()
        return stations_on_river 
    assert print_station_name('River D') == [['Station 6', 'Station 7', 'Station 8']]