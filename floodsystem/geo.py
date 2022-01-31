# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """This function uses haversine to calculate the distance between all the UK river monitoring stations
    and a given co-ordinate named in this function as p. We then return a list of the stations as instances
    of MonitoringStations and sort the list by the distances to the given co-ordinate"""
    stations_and_distance = []
    for station in stations:
        #Append to a new list a tuple of the station (MonitoringStation) and the distances to the given co-ordinate (float).
        stations_and_distance.append((station, haversine(p, station.coord)))
    return sorted_by_key(stations_and_distance, 1)
        
def stations_within_radius(stations, centre, r):
    """This function uses haversine to first compute the distance from the given centre to the station
    and then selects the stations which are closer than the given radius distance. The function then
    returns a list of stations (MonitoringStations) in an unsorted list."""
    stations_in_radius = []
    for station in stations:
        if haversine(centre, station.coord) < r:
            stations_in_radius.append(station)
    return stations_in_radius