# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list(False)

    #run inconsistency check
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    
    #Function to sort the list of inconsistent stations
    def inconsistent_stations_details(stations):
        """This function presents the station details in the required form i.e station name only
        The original function from the .geo file returns instances of MonitoringStation but we
        only want the name displayed (for readability reasons)"""
        inconsistent_stations_details = []
        #The function already filters out good station data so we only need to change it's format
        for station in stations:
            inconsistent_stations_details.append(station.name)
        #The deliverables ask for a alphabetically sorted list so we sort it before returning it
        inconsistent_stations_details.sort()
        return inconsistent_stations_details

    #Calling the function will not print the list so encase the function call in a print
    print(inconsistent_stations_details(inconsistent_stations))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()