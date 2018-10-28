#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:17:03 2018

@author: smitrao
"""

import pandas as pd
import numpy as np
import csv
from typing import List, Dict



'''Check frequency of accidents in the year (for example, do most accidents tend to occur in the month of January)?'''


YEAR_DICT = {}

with open('ksi.csv', newline='') as csvfile:
    eventreader = csv.DictReader(csvfile)
    for row in eventreader:
        if row['YEAR'] not in YEAR_DICT:
            YEAR_DICT.setdefault(row['YEAR'], [row['DATE']])
        else:
            YEAR_DICT[row['YEAR']] += [row['DATE']]

YEARS = list(YEAR_DICT.keys())
YEARS.sort() # displays years from 2007 to 2017

FREQ_DICT = {}

for year in YEAR_DICT:
    FREQ_DICT[int(year)] = []
    for date in YEAR_DICT[year]:
        FREQ_DICT[int(year)].append(int(date[5:7]))

for year in FREQ_DICT:

    FREQ_DICT[year].append({1:FREQ_DICT[year].count(1), 2:FREQ_DICT[year].count(2), \
                            3:FREQ_DICT[year].count(3), 4:FREQ_DICT[year].count(4), \
                            5:FREQ_DICT[year].count(5), 6:FREQ_DICT[year].count(6), \
                            7:FREQ_DICT[year].count(7), 8:FREQ_DICT[year].count(8), \
                            9:FREQ_DICT[year].count(9), 10:FREQ_DICT[year].count(10), \
                            11:FREQ_DICT[year].count(11), 12:FREQ_DICT[year].count(12)})

for y in FREQ_DICT:
    print(FREQ_DICT[y][-1])
