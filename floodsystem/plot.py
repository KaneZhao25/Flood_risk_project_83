# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
plotting data.

"""

from matplotlib import pyplot as plt
from datetime import datetime, timedelta

def plot_water_level(station, dates, levels):
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0], color = 'g', linestyle='--')
    plt.axhline(y=station.typical_range[1], color = 'r', linestyle='--')
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()