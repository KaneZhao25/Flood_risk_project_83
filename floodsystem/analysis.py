# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x0 = x[0]
    y = levels
    p_coeff = np.polyfit(x - x0, y, p)
    poly = np.poly1d(p_coeff)
    return poly, x0