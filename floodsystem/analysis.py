# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
import matplotlib
from matplotlib.cbook import print_cycles
import numpy as np
from floodsystem.station import MonitoringStation

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x0 = x[0]
    y = levels
    p_coeff = np.polyfit(x - x0, y, p)
    poly = np.poly1d(p_coeff)
    return poly, x0

def floodrisk(station, dates, levels):
    risk = 0
    #determine risk with relative water level
    if station.relative_water_level() > 1.5:
        risk += 3
    elif station.relative_water_level() > 1:
        risk += 2
    elif station.relative_water_level() > 0.5:
        risk += 1
    else:
        risk += 0

    #determine risk with tendency of change of water level
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, 1)
    gradient = p_coeff[0]
    if gradient > 1:
        risk += 2
    elif gradient > 0.5:
        risk += 1
    elif gradient < 0:
        risk -= 1
    else:
        risk += 0
    
    if risk <= 1:
        return 'low'
    elif risk == 2:
        return 'moderate'
    elif risk == 3:
        return 'high'
    else: 
        return 'severe'