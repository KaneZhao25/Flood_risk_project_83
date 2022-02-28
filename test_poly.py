# Copyright (C) 2022 Tianyu Zhao
#
# SPDX-License-Identifier: MIT
"""Unit test for the polyfit module"""

import numpy as np
from numpy import poly1d

def test_poly():
    x = np.linspace(1, 1000, 10000000)
    y = []
    for i in x:
        y.append(2*i**2)
    p_coeff = np.polyfit(x, y, 2)
    poly = poly1d(p_coeff)
    assert int(p_coeff[0]) == 2
    y = poly(10)
    return poly, p_coeff, y

print(test_poly())
