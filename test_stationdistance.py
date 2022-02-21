# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.unit_test_stations import build_unit_test_stations
from haversine import haversine

def test_distance():
    stations = build_station_list()
    station_distances = stations_by_distance(stations, (50.000, 0.8))
    assert isinstance(station_distances[0][1], float)
    assert isinstance(station_distances[0][0], MonitoringStation)
    assert sorted_by_key(station_distances, 1) == station_distances

def test_unit_stations_distance():
    unit_stations = build_unit_test_stations()
    sorted_unit_stations = stations_by_distance(unit_stations, (0., 0.))
    assert sorted_unit_stations[0][0].name == 'Test Station 1'
    assert sorted_unit_stations[1][0].name == 'Test Station 2'
    assert sorted_unit_stations[2][0].name == 'Test Station 3'
    assert sorted_unit_stations[3][0].name == 'Test Station 4'
    assert round(sorted_unit_stations[0][1], 3) == 0
    assert round(sorted_unit_stations[1][1], 3) == round(haversine((1., 0.), (0., 0.)), 3)
    assert round(sorted_unit_stations[2][1], 3) == round(haversine((0., 2.), (0., 0.)), 3)
    assert round(sorted_unit_stations[3][1], 3) == round(haversine((1., 2.), (0., 0.)), 3)

