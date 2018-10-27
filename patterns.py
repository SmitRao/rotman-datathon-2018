#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:17:03 2018

@author: smitrao
"""

import mathplotlib as mpl
import pandas as pd
import numpy as np
import csv
from typing import List, Dict



with open('ksi.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    i = 0
    for row in spamreader:
        print(row)
        break
    print(i)