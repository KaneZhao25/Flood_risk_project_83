# Copyright (C) 2021 Tornike Avaliani
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    #Find stations within the radius
    stations_in_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)

    #function to print the station details in a parsable form
    def stations_in_radius_details(stations):
        stations_in_radius_details = []
        for station in stations:
            stations_in_radius_details.append(station.name)
        stations_in_radius_details.sort()
        return stations_in_radius_details

    print(stations_in_radius_details(stations_in_radius))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()