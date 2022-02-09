# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
"""List for fake station data for test only"""

from floodsystem.station import MonitoringStation

def fake_station_list():

    fake_stations = []

    s_id1 = "test-s-id"
    m_id1 = "test-m-id"
    label1 = "station 1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "River A"
    town1 = "My Town"
    s1= MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    s_id2 = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "station 2"
    coord2 = (-2.0, 4.0)
    trange2 = (-2.3, 3.4445)
    river2 = "River B"
    town2 = "My Town"
    s2= MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    s_id3 = "test-s-id"
    m_id3 = "test-m-id"
    label3 = "station 3"
    coord3 = (-2.0, 4.0)
    trange3 = (-2.3, 3.4445)
    river3 = "River B"
    town3 = "My Town"
    s3= MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    s_id4 = "test-s-id"
    m_id4 = "test-m-id"
    label4 = "station 4"
    coord4 = (-2.0, 4.0)
    trange4 = (-2.3, 3.4445)
    river4 = "River C"
    town4 = "My Town"
    s4= MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    s_id5 = "test-s-id"
    m_id5 = "test-m-id"
    label5 = "station 5"
    coord5 = (-2.0, 4.0)
    trange5 = (-2.3, 3.4445)
    river5 = "River C"
    town5 = "My Town"
    s5= MonitoringStation(s_id5, m_id5, label5, coord5, trange5, river5, town5)

    s_id6 = "test-s-id"
    m_id6 = "test-m-id"
    label6 = "station 6"
    coord6 = (-2.0, 4.0)
    trange6 = (-2.3, 3.4445)
    river6 = "River D"
    town6 = "My Town"
    s6= MonitoringStation(s_id6, m_id6, label6, coord6, trange6, river6, town6)

    s_id7 = "test-s-id"
    m_id7 = "test-m-id"
    label7 = "station 7"
    coord7 = (-2.0, 4.0)
    trange7 = (-2.3, 3.4445)
    river7 = "River D"
    town7 = "My Town"
    s7= MonitoringStation(s_id7, m_id7, label7, coord7, trange7, river7, town7)

    s_id8 = "test-s-id"
    m_id8 = "test-m-id"
    label8 = "station 8"
    coord8 = (-2.0, 4.0)
    trange8 = (-2.3, 3.4445)
    river8 = "River D"
    town8 = "My Town"
    s8= MonitoringStation(s_id8, m_id8, label8, coord8, trange8, river8, town8)

    fake_stations.append(s1)
    fake_stations.append(s2)
    fake_stations.append(s3)
    fake_stations.append(s4)
    fake_stations.append(s5)
    fake_stations.append(s6)
    fake_stations.append(s7)
    fake_stations.append(s8)

    return fake_stations