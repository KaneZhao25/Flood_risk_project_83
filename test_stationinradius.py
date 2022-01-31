# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_distance():
    stations = build_station_list()
    station_distances = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert isinstance(station_distances[0], MonitoringStation)