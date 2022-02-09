# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
'''This file is made so I can call it over and over to create a standard set of MonitoringStation objects
Which I will use to run unit tests on.'''
def build_unit_test_stations():
    station1 = MonitoringStation(station_id='test_station_1',
                                measure_id='test_measure_id_1',
                                label='Test Station 1',
                                coord=(0., 0.),
                                typical_range=(1., 2.),
                                river='test_river_1',
                                town='test_town_1')
    station2 = MonitoringStation(station_id='test_station_2',
                                measure_id='test_measure_id_2',
                                label='Test Station 2',
                                coord=(1., 0.),
                                typical_range=(2., 1.),
                                river='test_river_2',
                                town='test_town_2')
    station3 = MonitoringStation(station_id='test_station_3',
                                measure_id='test_measure_id_3',
                                label='Test Station 3',
                                coord=(0., 2.),
                                typical_range=None,
                                river='test_river_3',
                                town='test_town_3')

    stations = [station1, station2, station3]
    return stations

