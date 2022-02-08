from test_fake_station_list import fake_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number

stations = fake_station_list()
print(rivers_with_station(stations))
print(stations_by_river(stations))
print(rivers_by_station_number(stations, 2))