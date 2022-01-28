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
    print(inconsistent_typical_range_stations(stations))
    


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()