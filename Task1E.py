# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT

from tkinter import N
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number

def run():
    """Requirements for Task 1E"""

    #Build list of stations
    stations = build_station_list(False)

    #Create list of stations with the function with given counter number
    N = 9
    rivers_station_number = rivers_by_station_number(stations, N)
    

    #Print the result
    print(rivers_station_number)
    
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()    