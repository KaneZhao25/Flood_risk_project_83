# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol=0.8):
    """This function returns the station (MonitoringStation object) and the realtive water level computed earlier on. The function
    Disregards any stations which have inconsistent data or are missing the relevant data. The function only returns tuples where
    the station has a relative water level greater than the tolerance margin."""
    stations_over_threshold = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > 100:
            continue
        elif station.relative_water_level() > tol:
            stations_over_threshold.append((station, station.relative_water_level()))
    return sorted_by_key(stations_over_threshold, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    """Because the stations_level_over_threshold already orders the stations into a list from highest relative water level to
    lowest, we can just return the station index (the 0th index) of the first 10 tuples from the over threshold list created in
    the stations_level_over_threshold function. We are required to return a station object so we return the entire 0th index."""
    most_risk_stations = []
    for station in stations_level_over_threshold(stations)[:N]:
        most_risk_stations.append(station[0])
    return most_risk_stations