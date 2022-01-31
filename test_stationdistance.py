# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_distance():
    stations = build_station_list()
    station_distances = stations_by_distance(stations, (50.000, 0.8))
    assert isinstance(station_distances[0][1], float)
    assert isinstance(station_distances[0][0], MonitoringStation)
    assert sorted_by_key(station_distances, 1) == station_distances
