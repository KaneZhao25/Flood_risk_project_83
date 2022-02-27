# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
from unicodedata import name
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import floodrisk
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
import datetime

def run():
    stations = build_station_list()
    update_water_levels
    low = set()
    moderate = set()
    high = set()
    severe = set()
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        risk = floodrisk(station, dates, levels)
        if risk == 'severe':
            severe.add(station.town)
        elif risk == 'high':
            high.add(station.town)
        elif risk == 'moderate':
            moderate.add(station.town)
        elif risk == 'low':
            low.add(station.town)
    print(severe)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
