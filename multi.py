#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import string
import os


latColumn = string.lowercase.index('q') # determine index that corresponds to Excel Column letter (user lower case)
longColumn = string.lowercase.index('r') # Does not work for AA, BB, ...
for root, dirs, files in os.walk(".", topdown=False):
    for filename in files:
        if filename.endswith('.xlsx'):            
	  data = pd.read_excel(filename, 'Sheet1', parse_cols=[latColumn,longColumn])
	  data = data.replace(to_replace="None", value=0)
	  csvOut = "/home/map_data/map_data.csv"
	  f=open(csvOut, 'a')
	  data[:65534].to_csv(f, index=False, header=False)