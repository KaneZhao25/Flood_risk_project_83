# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.unit_test_stations import build_unit_test_stations

def test_distance():
    stations = build_station_list()
    station_distances = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert isinstance(station_distances[0], MonitoringStation)

def test_unit_stations_radius():
    unit_stations = build_unit_test_stations()
    unit_stations_in_radius = stations_within_radius(unit_stations, (0., 0.), 200)
    assert len(unit_stations_in_radius) == 2
    assert unit_stations_in_radius[0].name == 'Test Station 1'
    assert unit_stations_in_radius[1].name == 'Test Station 2'