# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from operator import itemgetter
from xml.dom.minidom import Element
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
        if haversine(centre, station.coord) <= r:
            stations_in_radius.append(station)
    return stations_in_radius

def rivers_with_station(stations):
    """This function provides the list of rivers with a monitoring station."""
    station_rivers = set()
    for station in stations:
        station_rivers.add(station.river)
    return station_rivers

def stations_by_river(stations):
    """This function gives a dictionary that maps the rivers with the stations."""
    rivers_dic = {}
    for rivers in rivers_with_station(stations):
        rivers_dic[rivers] = []
    for station in stations:
        rivers_dic[station.river].append(station.name)
    return rivers_dic
        
def rivers_by_station_number(stations, N):
    """This function determines the number of stations by rivers and sorts the list by the number of stations."""
    station_number = []
    river_dic = stations_by_river(stations)
    for river_number in river_dic:
        k = (river_number, len(stations_by_river(stations)[river_number]))
        station_number.append(k)
    sorted_station_number_list = sorted_by_key(station_number, 1, reverse=True)
    #print(sorted_station_number_list)
    counter = N
    while sorted_station_number_list[counter - 1][1] == sorted_station_number_list[counter][1]:
         counter += 1
         #print(counter)
    return sorted_station_number_list[:counter]





    

