#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from os import listdir
from os.path import join
#delete old map_data files
os.remove("/home/map_data/map_data.csv")


#delete old files in test folder.
dir = "/test"
test=os.listdir(dir)

for item in test:
    if item.endswith(".xlsx"):
        os.remove(join(dir, item))