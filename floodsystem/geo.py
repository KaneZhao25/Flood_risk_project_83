# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    stations_and_distance = []
    for station in stations:
        stations_and_distance.append((station.name, haversine(p, station.coord)))
    sorted_stations_and_distance = sorted(stations_and_distance, key=lambda tup: tup[1])
    return sorted_stations_and_distance
        