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
    return sorted_by_key(stations_and_distance, 1)
        