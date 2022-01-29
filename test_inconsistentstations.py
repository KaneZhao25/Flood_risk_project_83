# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""

import datetime
from xmlrpc.client import boolean

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list


from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def test_inconsistentstations():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    assert isinstance(inconsistent_stations[0], MonitoringStation)
    assert isinstance(inconsistent_stations[0].typical_range_consistent(), boolean)