# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list(False)

    #Calculate distances to stations
    station_distances = stations_by_distance(stations, (52.2053, 0.1218))

    #set up a function which prints station name, station town and distance from the inputted co-ordinates
    def show_station_distance(station_distances):
        """This function presents the data in the way required in the deliverables. station name
        station town and the distance to the co-ordinates entered"""
        station_distance_details = []
        for station_distance in station_distances:
            station_distance_details.append((station_distance[0].name, station_distance[0].town, station_distance[1]))
        #We use the sorted_by_key function in the geo file to sort the tuples by station distances
        return station_distance_details
    
    #Print station details for the 10 closest stations
    print(show_station_distance(station_distances[0:10]))
    #Print station details for the 10 farthest stations
    print(show_station_distance(station_distances[-10:]))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()