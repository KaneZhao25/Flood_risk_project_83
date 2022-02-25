# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
plotting data.

"""

from matplotlib import pyplot as plt
from datetime import date, datetime, timedelta
from floodsystem.analysis import polyfit
import matplotlib
import numpy as np

def plot_water_level(station, dates, levels):
    """This function plots relative water level for the last few days at a given station and also plots the typical
    High and Low level at the station of interest."""
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0], color = 'g', linestyle='--')
    plt.axhline(y=station.typical_range[1], color = 'r', linestyle='--')
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x1 = np.linspace(x[0], x[-1], 1000)
    poly, d0 = polyfit(dates, levels, p)
    
    plt.plot(x1, poly(x1))
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.legend
    plt.show