# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""

    #Build list of stations
    stations = build_station_list(False)

    #Build lists of rivers with stations
    river_with_station = []
    for element in rivers_with_station(stations):
        river_with_station.append(element)

    #Sort the rivers in alphabetical order
    river_with_station.sort()

    #Print the numbers of the rivers and the first 10 rivers
    print(len(river_with_station))
    print(river_with_station[0:9])

    #Define a function to create lists of stations on rivers
    def print_station_name(river):

        #Build list of stations on a given river
        river_dic = stations_by_river(stations)
        stations_on_river = []
        for element in river_dic[river]:
            stations_on_river.append(element)

        #Sort the list of stations
        stations_on_river.sort()
        return stations_on_river 
    
    print(print_station_name('River Aire'))
    print(print_station_name('River Cam'))
    print(print_station_name('River Thames'))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()