#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 09:16:13 2018

@author: Quantum
"""

# install geopandas: conda install -c conda-forge geopandas
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import re
# import myFunc

fpcounty='NCFlood_Effective_Wake_SHP\V_E_HYDROGAGE.shp'
ctdata=gpd.read_file(fpcounty)

import sys
print(sys.version)