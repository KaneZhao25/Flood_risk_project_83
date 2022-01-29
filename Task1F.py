# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    #run inconsistency check
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    
    #Function to sort the list of inconsistent stations
    def inconsistent_stations_details(stations):
        inconsistent_stations_details = []
        for station in stations:
            inconsistent_stations_details.append(station.name)
        inconsistent_stations_details.sort()
        return inconsistent_stations_details

    print(inconsistent_stations_details(inconsistent_stations))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()